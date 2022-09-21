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

    return boto3.client("s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)


def fetch_bucket_data():
    conn = boto3.session.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    s3 = conn.resource('s3')
    return s3.Bucket(BUCKET_NAME)

