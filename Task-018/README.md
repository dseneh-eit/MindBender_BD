# Task 018

## Pipeline #3: Kafka Producer & Consumer


### Kafka Consumer

The goal is to create a Kafka Producer to get data from a new API and a consumer to have data stored in db.
For this project, I used the [Marta](https://www.itsmarta.com/app-developer-resources.aspx) API.

#### Task:
- Create a Kafka topic with 3 partition, 3 replication factor (3 brokers)
- Create a producer in python to injest data from api to the topic
- Create a consumer to consume data from the kafka topic of the three brokers
- Create the consumer using scala (using sbt)
- Spark processing: Extract needed columns from the data received from the topic
- Have the consumer compiled in .jar file format
