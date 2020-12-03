from datetime import datetime
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import (StructType, StructField, StringType,FloatType, DateType, IntegerType)
from pyspark.sql.functions import when, udf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession


global ss
    
def run_process():
    
    sc = SparkContext("local[*]", )
    ssc = StreamingContext(sc,10)
    ss = SparkSession.builder \
    .appName("MartaBus") \
        .master("local[*]").getOrCreate()
            # .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
            #         .config("hive.metastore.uris", "thrift://localhost:9083") \
            #             .enableHiveSupport().getOrCreate()


    ks = KafkaUtils.createStream(ssc, "localhost:2181","transdata", {"transdata" :1})
    passed = ks.flatMap(lambda y: json.loads(y[1]))
    
    def process(rdd):
        if not rdd.isEmpty():
            df = ss.createDataFrame(rdd)
            df.show()

            # df.write.saveAsTable(name ="books.goodreadsbooks", format="hive", mode="overwrite")

    passed.foreachRDD(process)
    ssc.start()
    ssc.awaitTermination()


if __name__ == "__main__":
    run_process()