import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.streaming._
import org.apache.spark.sql.types._

object martabus {
    def main(args: Array[String]): Unit = {

    val spark = SparkSession
        .builder.appName("MartaBus")
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse")
        .config("hive.metastore.uris", "thrift://localhost:9083")
        .enableHiveSupport()
        .getOrCreate()
                    
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

        import spark.implicits._
        val sc = spark
            .readStream
            .format("kafka")
            .option("kafka.bootstrap.servers", "localhost:9099,localhost:9098,localhost:9097")
            .option("subscribe", "transdata")
            .load()
            .select($"value" cast "string" as "json")
            .select(from_json($"json", schema1) as "data")
            .select("data.*")

    val query = sc
            .writeStream
            .outputMode(OutputMode.Append())
            .format("parquet")
            .option("checkpointLocation", "/tmp/checkpoint")
            .option("table", "transdb.transbus")
            .start("hdfs://master1:9000/user/hive/warehouse/data/trans")

    query.awaitTermination()
    
}
}
 
