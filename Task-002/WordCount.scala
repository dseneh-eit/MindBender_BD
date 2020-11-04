import scala.io.Source
import java.io._
import java.io.PrintWriter

import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.{FileSystem, Path}

object WordCount extends App {

  def wordCnt: Map[String, Int] = {
    val filename = "Task-001/Shakespeare.txt"
    lazy val bufferSource = Source.fromFile(filename)
    bufferSource.getLines
      .filter(_.nonEmpty)
      .flatMap(_.split("""\W+""")).toSeq
      .groupBy(_.toLowerCase())
      .mapValues(_.size)
//      .sortWith { case ((_, v0), (_, v1)) => v0 > v1 }
  }

  def write_file(file: Map[String, Int], path: String) = {
    val writer = new PrintWriter(new File(path))
    file.foreach{
      case (k, v) => writer.write(k + ": " + v + "\n")
    }
  }

  write_file(wordCnt, "output_scala.txt")
    wordCnt.foreach {
      case (word, count) => println(word + ": " + count)
    }

  def
}