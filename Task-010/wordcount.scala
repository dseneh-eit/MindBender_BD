import scala.io.Source
import java.io._
import java.io.PrintWriter

// import org.apache.hadoop.conf.Configuration
// import org.apache.hadoop.fs.{FileSystem, Path}


object wordcount extends App {
    println("Working")
  def wordCnt: Map[String, Int] = {
    val filename = "Task-001/Shakespeare.txt"
    println("getting file...")
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


//   def mainRun(args: Array[String]): Unit = {
    // write_file(wordCnt, "output_scala2.txt")
    wordCnt.foreach {
      case (word, count) => println(word + ": " + count)
    }

//   }
}