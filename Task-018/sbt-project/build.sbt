name := "martabus"
version := "1.4"
scalaVersion := "2.11.8"

libraryDependencies ++= Seq(
    "org.apache.spark" %% "spark-core" % "2.3.2" % "provided",
    "org.apache.spark" %% "spark-sql" % "2.3.2" % "provided"
)
