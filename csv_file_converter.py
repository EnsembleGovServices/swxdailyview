import json
import os
from io import StringIO

import boto3
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

s3_client = boto3.client("s3", aws_access_key_id=ACCESS_KEY,
                         aws_secret_access_key=SECRET_KEY)

import pandas as pd

file_name = 'high latitude k index/High Latitude K Index  2022.09.08 1702.csv'
response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
raw_data = response.get('Body')
data = raw_data.read().decode('UTF-8')
print(data)
print(">>>>",type(data))
df = pd.read_csv(StringIO(data))
print(df)
print(df.iloc[0]['TimeStamp'])