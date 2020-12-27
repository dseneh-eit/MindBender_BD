from datetime import datetime
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import (StructType, StructField, StringType, FloatType, DateType, IntegerType, TimestampType)
from pyspark.sql.functions import explode, when, udf, posexplode, col, struct, date_format
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession


def run_process():
    global ss

    sc = SparkContext("local[*]", )
    ssc = StreamingContext(sc, 10)
    ss = SparkSession.builder \
        .appName("YouTube") \
        .master("local[*]") \
        .getOrCreate()

    categories = {1: "Film & Animation", 2: "Autos & Vehicles", 10: "Music", 15: "Pets & Animals",
                  17: "Sports", 19: "Travel & Events", 20: "Gaming", 22: "People & Blogs", 23: "Comedy",
                  24: "Entertainment", 25: "News & Politics", 26: "Howto & Style", 27: "Education",
                  28: "Science & Technology", 29: "Nonprofits & Activism"}

    countries = {"US": "United States", "GB": "Great Britain", "IN": "India", "DE": "Germany", "CA": "Canada",
                 "FR": "France",
                 "KR": "South Korea", "RU": "Russia", "JP": "Japan", "BR": "Brazil", "MX": "Mexico"}

    # Define custom function and register as spark udf respectively
    def getCategory(x):
        return categories[x]

    getCat = udf(lambda x: getCategory(x))
    ss.udf.register("getCat", getCat)

    def getCountry(x):
        return countries[x]

    getCon = udf(lambda x: getCountry(x))
    ss.udf.register("getCon", getCon)

    def replaceNull(x):
        if x is None:
            x = 0
        return x

    replaceNull = udf(lambda x: replaceNull(x))
    ss.udf.register("replaceNull", replaceNull)

    ks = KafkaUtils.createStream(ssc, "localhost:2181", "youtube", {"youtube": 1})
    parsed1 = ks.map(lambda y: json.loads(y[1]))

    def process(rdd):
        if not rdd.isEmpty():
            df = ss.createDataFrame(rdd)
            df2 = df.withColumn("snippet", col("snippet"))
            dataFrame = df2.select(df2["snippet.publishedAt"].alias("published_at"),
                                   df2["snippet.channelId"].alias("channel_id"),
                                   df2["snippet.title"].alias("video_title"),
                                   df2["snippet.channelTitle"].alias("channel_title"),
                                   df2["snippet.categoryId"].alias("category_id"),
                                   df2["statistics.viewCount"].alias("view_count"),
                                   df2["statistics.likeCount"].alias("like_count"),
                                   df2["statistics.dislikeCount"].alias("dislike_count"),
                                   df2["statistics.favoriteCount"].alias("favorite_count"),
                                   df2["statistics.commentCount"].alias("comment_count"),
                                   df2["country.code"])

            dataFrame = dataFrame.withColumn("category_id", dataFrame["category_id"].cast(IntegerType()))
            dataFrame = dataFrame.withColumn("view_count", dataFrame["view_count"].cast(IntegerType()))
            dataFrame = dataFrame.withColumn("like_count", dataFrame["like_count"].cast(IntegerType()))
            dataFrame = dataFrame.withColumn("dislike_count", dataFrame["dislike_count"].cast(IntegerType()))
            dataFrame = dataFrame.withColumn("favorite_count", dataFrame["favorite_count"].cast(IntegerType()))
            dataFrame = dataFrame.withColumn("comment_count", dataFrame["comment_count"].cast(IntegerType()))
            dataFrame = dataFrame.withColumn("category", getCat("category_id"))
            dataFrame = dataFrame.withColumn("pub_date",
                                             date_format(dataFrame["published_at"].cast(dataType=TimestampType()),
                                                         "yyyy-MM-dd"))
            dataFrame = dataFrame.withColumn("pub_month",
                                             date_format(dataFrame["published_at"].cast(dataType=TimestampType()),
                                                         "MMMM"))
            dataFrame = dataFrame.withColumn("pub_day",
                                             date_format(dataFrame["published_at"].cast(dataType=TimestampType()),
                                                         "dd"))
            dataFrame = dataFrame.withColumn("pub_year",
                                             date_format(dataFrame["published_at"].cast(dataType=TimestampType()),
                                                         "yyyy"))
            dataFrame = dataFrame.withColumn("pub_time",
                                             date_format(dataFrame["published_at"].cast(StringType()), "hh:mm"))
            dataFrame = dataFrame.withColumn("country", getCon("code"))

            dataFrame.fillna({'dislike_count': 0, 'like_count': 0, 'favorite_count': 0, 'comment_count': 0})

            dataFrame.write.format('jdbc').options(
                url='jdbc:mysql://localhost/bigdata',
                driver='com.mysql.jdbc.Driver',
                dbtable='youtube',
                user='root',
                password='root').mode('append').save()
            # dataFrame.write.jdbc(url="jdbc:mysql://localhost:3333/bigdata"
            #       "?user=root&password=P@55wOrd",
            #   table="my_table",
            #   mode="append",
            #   properties={"driver": 'com.mysql.jdbc.Driver'})

            # dataFrame.write.format("jdbc").option("url", "jdbc:mysql://localhost/bigdata") \
            #     .option("driver", "com.mysql.jdbc.Driver") \
            #         .option("dbtable", "youtubestats") \
            #         .option("user", "root") \
            #         .option("password", "P@55wOrd") \
            #         .save()

            dataFrame.show(50)
            # dataFrame.printSchema()

    parsed1.foreachRDD(process)

    ssc.start()
    ssc.awaitTermination()


if __name__ == "__main__":
    run_process()

#  |-- published_at: string (nullable = true)
#  |-- channel_id: string (nullable = true)
#  |-- video_title: string (nullable = true)
#  |-- channel_title: string (nullable = true)
#  |-- category_id: integer (nullable = true)
#  |-- view_count: integer (nullable = true)
#  |-- like_count: integer (nullable = true)
#  |-- dislike_count: integer (nullable = true)
#  |-- favorite_count: integer (nullable = true)
#  |-- comment_count: integer (nullable = true)
#  |-- code: string (nullable = true)
#  |-- category: string (nullable = true)
#  |-- pub_date: string (nullable = true)
#  |-- pub_month: string (nullable = true)
#  |-- pub_day: string (nullable = true)
#  |-- pub_year: string (nullable = true)
#  |-- pub_time: string (nullable = true)
#  |-- country: string (nullable = true)
