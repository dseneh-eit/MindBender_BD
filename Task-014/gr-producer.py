import pandas as pd 
import json
from kafka import KafkaProducer, KafkaClient

f = open("file.json").read()
d = json.loads(f)
data = json.dumps(d)

producer = KafkaProducer(bootstrap_servers=['localhost:9099'])

def fetch():
    print(f"Sending data to topic...")
    producer.send("goodreadsbooks", data.encode('utf-8'))
    print("Done!")
    return True

if __name__=="__main__":
    fetch()
    producer.flush()


