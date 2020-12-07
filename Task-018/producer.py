import requests, json
from kafka import KafkaProducer
import threading, sys
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost:9099','localhost:9098','localhost:9097'])
SEC = 6.0
class GetData():
    def __init__(self, counter=1):
        self.counter = counter

    def fetch_data(self):
        count = self.counter
        print("", end=f"\rSending request: {count} ")
        url = f"http://developer.itsmarta.com/BRDRestService/BRDRestService.svc/GetAllBus"
        buses = json.loads(requests.get(url).text)

        sys.stdout.flush()
      
        if len(buses) >2:
            for bus in buses:
                producer.send("transdata", json.dumps(bus).encode('utf-8'))
                producer.flush()
            self.counter+=1
        else:
            self.counter = "No data, retrying..."
        threading.Timer(SEC, self.fetch_data).start()
        return True

 
if __name__=="__main__":
    now = datetime.now()
    fetch = GetData()
    print(f"*****STREAMING STARTED*****")
    print(f"Timestamp: {now.strftime('%D at %H:%M:%S')}")
    print(f'A new API request will be sent every {SEC}sec')
    print('----------------------------------------------')
    print(" ")
    fetch.fetch_data()