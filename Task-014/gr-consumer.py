from datetime import datetime
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import (StructType, StructField, StringType,FloatType, DateType, IntegerType)
from pyspark.sql.functions import when, udf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession

COL_NAMES = ['title', 'rating_dist1', 'page_num', 'rating_dist4', 'publish_month',
       'publish_day', 'publisher', 'review_count', 'publish_year', 'language',
       'authors', 'rating', 'rating_dist2', 'rating_dist5', 'isbn',
       'rating_dist3']

def set_schema():
    slst = []
    for c == 'pages_num':
        if c in INT:
            slst.append(StructField(c, IntegerType(), True))
        elif c == 'rating':
            slst.append(StructField(c, FloatType(), True))
        else:
            slst.append(StructField(c, StringType(), True))
    
    return StructType(slst)
schema = set_schema()

def get_rating(n):
    r = []
    for i in range(int(n)):
        r+="⭐"   
    decimal = n % 1
    if decimal >= .5: 
        r+="⭐"
    return str(''.join(r))
    
    
    
def run_process():
    global ss
    
    sc = SparkContext("local[*]", )
    ssc = StreamingContext(sc,10)
    ss = SparkSession.builder \
    .appName("GoodReads") \
        .master("local[*]") \
            .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
                    .config("hive.metastore.uris", "thrift://localhost:9083") \
                        .enableHiveSupport().getOrCreate()


    ks = KafkaUtils.createStream(ssc, "localhost:2181","goodreadsbooks", {"goodreadsbooks" :1})
    passed = ks.flatMap(lambda y: json.loads(y[1]))
    
    def process(rdd):

        if not rdd.isEmpty():
            schem = set_schema()
            df = ss.createDataFrame(rdd, schema=schem)
            rate_star =  udf(lambda x: get_rating(x))
            ss.udf.register("rate_star", rate_star)
            rating = df.withColumn("stars", rate_star(df.rating))
            rating.show()
            rating.write.saveAsTable(name ="books.goodreadsbooks", format="hive", mode="overwrite")

    passed.foreachRDD(process)
    ssc.start()
    ssc.awaitTermination()


if __name__ == "__main__":
    run_process()