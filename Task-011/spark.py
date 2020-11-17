from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    sc = SparkContext("local", "Word Count Task").getOrCreate()
    f = "/Desktop/BigData/MindBender_BD/Task-001/Shakespeare.txt"
    words = sc.textFile(f).flatMap(lambda line: line.split(" "))

    wordCounts = words.map(lambda word: (
        word, 1)).reduceByKey(lambda a, b: a + b)
    wordCounts.saveAsTextFile(
        "hdfs://master:9000/wordcount/output")
