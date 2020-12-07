import boto3
import pydoop.hdfs as hdfs

s3 = boto3.resource('s3')
bucket = 'bd-mindbender0001'

def upload_file():
  f = hdfs.open('hdfs://master1:9000/data/MOCK_DATA.csv')
  s3.Bucket(bucket).put_object(Key='muck.csv', Body=f)
  return "File uploaded!"

def download_file():
  s3.Bucket(bucket).download_file(Key='gtr.png', Filename='gtr.png')
  return "File has been downloaded!"


if __name__=="__main__":
  upload_file()
  download_file()