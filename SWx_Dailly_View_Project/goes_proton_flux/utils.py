import os

import boto3
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")


def fetch_last_modified_proton_flux_file():
    bucket_name = BUCKET_NAME
    conn = boto3.session.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    s3 = conn.resource('s3')
    bucket_data = s3.Bucket(bucket_name)
    lis = []
    for x in bucket_data.objects.filter(Prefix='proton flux/'):
        lis.append(x.last_modified)
    for x in bucket_data.objects.filter(Prefix='proton flux/'):
        if x.last_modified == lis[-1]:
            latest_file = x.key

    return latest_file
