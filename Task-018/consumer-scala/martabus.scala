import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.streaming._
import org.apache.spark.sql.types._

// import org.apache.spark.sql.functions.from_json

case class BusData(adherence: String, blickid: String, 
                    block_abbr: String, direction: String, latitude: String, longitude: String,
                    msgtime: String, route: String, stopid: String, timepoint: String, tripid: String,
                    vehicle: String
                    )

object martabus {
    def main(args: Array[String]): Unit = {
        
        val spark = SparkSession
        .builder.appName("MartaBus").getOrCreate()


    val schema1 = StructType(List(
            StructField("ADHERENCE", StringType, true),
            StructField("BLOCKID", StringType, true),
            StructField("BLOCK_ABBR", StringType, true),
            StructField("DIRECTION", StringType, true),
            StructField("LATITUDE", StringType, true),
            StructField("LONGITUDE", StringType, true),
            StructField("MSGTIME", StringType, true),
            StructField("ROUTE", StringType, true),
            StructField("STOPID", StringType, true),
            StructField("TIMEPOINT", StringType, true),
            StructField("TRIPID", StringType, true),
            StructField("VEHICLE", StringType, true)
            ))
    //   val schema1 = StructType(List(
    //         StructField("adherence", StringType, true),
    //         StructField("blockid", StringType, true),
    //         StructField("block_abbr", StringType, true),
    //         StructField("direction", StringType, true),
    //         StructField("latitude", StringType, true),
    //         StructField("longitude", StringType, true),
    //         StructField("msgtime", StringType, true),
    //         StructField("route", StringType, true),
    //         StructField("stopid", StringType, true),
    //         StructField("timepoint", StringType, true),
    //         StructField("tripid", StringType, true),
    //         StructField("vehicle", StringType, true)
    //         ))

        import spark.implicits._
        val rdd = spark
            .readStream
            .format("kafka")
            .option("kafka.bootstrap.servers", "localhost:9099,localhost:9098,localhost:9097")
            .option("subscribe", "transdata")
            .load()
            .select($"value" cast "string" as "json")
            // .select("json.*")
            .select(from_json($"json", schema1) as "data")
            .select("data.*")
            

    // val data = rdd.selectExpr("CAST(value AS STRING)").as[String].toDF()
        
    // import spark.implicits._
    // val df = spark.readStream
    //     .format("kafka")
    //     .option("kafka.bootstrap.servers", "localhost:9099,localhost:9098,localhost:9097")
    //     .option("subscribe", "transdata")
    //     .load()
    // val rsvpJsonDf = df.selectExpr("CAST(value as STRING)")
    // val data = rsvpJsonDf.select(from_json($"value", schema1).as("transdata"))

    // val expandedData = rdd.selectExpr("explode(json) as data").select("json.*")
    // val data = rdd.selectExpr("CAST(value AS STRING)").as[String]
    val expandedData = rdd //.flatMap(row => row.split(","))

   
        // .map(row => BusData(
        //     row(1).toString,
        //     row(2).toString,
        //     row(3).toString,
        //     row(4).toString,
        //     row(5).toString,
        //     row(6).toString,
        //     row(7).toString,
        //     row(8).toString,
        //     row(9).toString,
        //     row(10).toString,
        //     row(11).toString,
        //     row(12).toString
        // ))

        val query = expandedData
            .writeStream
            .outputMode("update")
            .format("console")
            .start()
    



    query.awaitTermination()
    
}
}

