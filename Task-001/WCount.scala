import scala.io.Source
import java.io._
import java.io.PrintWriter

object WCount extends App {

  def load_file(file: String): List[String] = {
    val w = """[a-zA-Z0-9]+""".r
    lazy val bufferSource = Source.fromFile(file).getLines.flatMap(w.findAllIn).toList
    return convert_file(bufferSource)
  }

  def convert_file(file: List[String]): List[String] = {
    val f = for (t <- file) yield t.toLowerCase
    return f
  }

  def count(file: List[String]): Map[String, Int] = {
    val f = convert_file(file)
    f.toSet.map((word: String) => (word, file.count(_ == word))).toMap
  }

  val f = "Shakespeare.txt"
  lazy val c = load_file(f)
  println(count(c))
//  println(f)

  def write_file(file: Map[String, Int], path: String) = {
    val writer = new PrintWriter(new File(path))
    file.foreach{
      case (k, v) => writer.write(k + " " + v + "\n")
    }
  }
}