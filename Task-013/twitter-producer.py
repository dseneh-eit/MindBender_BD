from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer  # KafkaClient

ACCESS_TOKEN = "259212489-w4I4m8egfeyhNkBz2ZeRC7FA9ttghgVyos1r1wvX"
TOKEN_SECRET = "iA1bGH4BJBvuRwtytu2CfW3GHQfzzsoghLa8JAXsCQZwQ"
CONSUMER_KEY = "tI9ch4zHFsFlh4wA7mVfZA2tO"
CONSUMER_SECRET = "jKKxWoj3iVvHhMDZLZiLjlNymLgQiCEHlkPjudCHTEfJBP95Vz"
TOPIC = "tweets"


class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send(TOPIC, data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print(status)


# kafka = KafkaClient("localhost:9099")
producer = KafkaProducer(bootstrap_servers=['localhost:9099'])
l = StdOutListener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
stream = Stream(auth, l)
stream.filter(track=TOPIC)
