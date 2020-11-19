import org.apache.spark._

object wordCount {
  def main(args: Array[String]): Unit = {
    val f = "/home/user/Desktop/BigData/In-Class/Shakespeare.txt"

    val conf = new SparkConf().setAppName("WordCount").setMaster("local")
    val sc = new SparkContext(conf)
    val input = sc.textFile(f)
    val count = input.flatMap(line=>line.split(" "))
      .map(word=>(word, 1))
      .reduceByKey(_+_)
    count.saveAsTextFile("output")
    println("Count complete!")
  }
}