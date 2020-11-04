import scala.io.Source

object WordCount extends App {

  def wordCnt: Map[String, Int] = {
    val filename = "Shakespeare.txt"
    lazy val bufferSource = Source.fromFile(filename)
    bufferSource.getLines
      .filter(_.nonEmpty)
      .flatMap(_.split("""\W+""")).toSeq
      .groupBy(_.toLowerCase())
      .mapValues(_.size)
//      .sortWith { case ((_, v0), (_, v1)) => v0 > v1 }
  }

    wordCnt.foreach {
      case (word, count) => println(word + ": " + count)
    }

}