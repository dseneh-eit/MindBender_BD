import requests, json
from kafka import KafkaProducer
import os, time
from dotenv import load_dotenv
load_dotenv()


key = os.getenv('AUTH_KEY')
country = ['US','GB','IN','CA','FR','KR','RU','JP','BR','MX']

producer = KafkaProducer(bootstrap_servers=['localhost:9099','localhost:9098','localhost:9097'])
topic = 'youtube'


for code in country:

    url = f"https://www.googleapis.com/youtube/v3/videos?part=id,statistics,snippet&chart=mostPopular&regionCode={code}&maxResults=50&key={key}"
    results = json.loads(requests.get(url).text)

    # f = open('sample.json').read()
    # results = json.loads(f)
    data_list = results['items'] 
    
    for data in data_list:
        data["country"] = {"code": code}
        producer.send(topic, json.dumps(data).encode('utf-8'))
        producer.flush()
        # print(data)
        print(f"Sent for {code}")
        time.sleep(1)
    time.sleep(1)