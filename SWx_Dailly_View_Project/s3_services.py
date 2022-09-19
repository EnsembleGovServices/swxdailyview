import os

import boto3
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")


def get_s3_client():
    """
        Creates the s3 buckets client
    """

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY)

    return s3_client


def fetch_bucket_data():
    bucket_name = BUCKET_NAME
    conn = boto3.session.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    s3 = conn.resource('s3')
    bucket_data = s3.Bucket(bucket_name)
    return bucket_data
