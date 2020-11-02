import scala.io.Source

object WordCount extends App {

  def wordCnt = {
    lazy val filename = "Shakespeare.txt"
    lazy val bufferSource = Source.fromFile(filename)
    bufferSource.getLines
      .filter(_.nonEmpty)
      .flatMap(_.split("""\W+""")).toSeq
      .groupBy(_.toLowerCase())
      .view.mapValues(_.size).toSeq
      .sortWith { case ((_, v0), (_, v1)) => v0 > v1 }
  }
  wordCnt.foreach {
    case (word, count) => println(f"$word%-8s $count%6d")
  }
}
