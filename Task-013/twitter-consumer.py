from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
from json import loads

def runSpark():
    global ss
    def process(rdd):
        if not rdd.isEmpty():    
            df = ss.createDataFrame(rdd, schema=["id", "text"])
            df.show()
            print(rdd)
            df.write.saveAsTable(name="twitter_api_db", format="hive", node="append")

    sc = SparkContext("local[*]", "TweetAPI")
    ssc = StreamingContext(sc, 10)

    ss = SparkSession.builder.enableHiveSupport().getOrCreate()
    kafkaStream = KafkaUtils.createStream(
        ssc, 'localhost:2181', 'tweets', {'tweets': 1})

    parsed = kafkaStream.map(lambda v: loads(v[1]))
    fit = parsed.filter(lambda v: v.get("lang") == "eng").map(lambda v: (v.get("id"), v.get("text")))

    fit.map(lambda x: "Tweets %s" % x).pprint()
    

    fit.foreachRDD(process)
 

    ssc.start()
    ssc.awaitTermination()


if __name__ == "__main__":
    runSpark()
    

