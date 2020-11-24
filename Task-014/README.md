# Task 014

## Creating a Kafka Producer & Consumer


### Kafka Producer

The goal is to create a Kafka Producer to get data from our personal APIs.
In my case, I used the [Goodreads Books API](https://www.goodreads.com/api).

#### Task:
- Create a Kafka topic with 1 partition, 1 replication factor
- Injest data from the api to the topic created


### Kafka Consumer

The goal is to stream the data that was injested within the topic created
and perform some spark streaming processing, and lastly have the data stored to a Hive table.

#### Task:
- Create a Hive table
- Load the json data from the topic created using pyspark
- Convert the Kafka Streaming data (loaded in json format) to rdd
- Create a pyspark schema and convert the rdd to dataframe
- Save dataframe as a Hive table
- For the processing aspect:
 - I created a udf and convert the value of the 'ratings' column to display actual stars: '⭐'.
