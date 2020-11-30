import requests
from kafka import KafkaProducer
import threading, sys

producer = KafkaProducer(bootstrap_servers=['localhost:9099'])

class GetData():
    def __init__(self, counter=1):
        self.counter = counter

    def fetch_data(self):
        count = self.counter
        txt = f"Sending request:"
        print("", end=f"\r{txt} {count} ")
        url = f"http://developer.itsmarta.com/BRDRestService/BRDRestService.svc/GetAllBus"
        bus = requests.get(url).text
        sys.stdout.flush()

        # Send response to topic only if it is not an empty [], retry...
        if len(bus) >2:
            producer.send("atlBuses", bus.encode('utf-8'))
            producer.flush()
            self.counter+=1
        else:
            self.counter = "No data, retrying..."
        
        # Send a new request every minute (60sec)
        threading.Timer(60.0, self.fetch_data).start()
        return True

if __name__=="__main__":
    fetch = GetData()
    print(f"Started streaming...")
    fetch.fetch_data()