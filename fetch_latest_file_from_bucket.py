import os

import boto3
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")


# bucket_name = "swxdailyview"
# conn = boto3.session.Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
# s3 = conn.resource('s3')
# test_buc = s3.Bucket(bucket_name)
# x = None
# lis = []
# for x in test_buc.objects.filter(Prefix='kp index/'):
#     # print("this is x: ",x)
#     lis.append(x.last_modified)
# for x in test_buc.objects.filter(Prefix='kp index/'):
#     if x.last_modified == lis[-1]:
#         print("this is x: ",x)
#         print("the data is: ",x.last_modified,lis[-1])

def fetch_last_modified_kp_forecast_file():
    bucket_name = "swxdailyview"
    conn = boto3.session.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    s3 = conn.resource('s3')
    test_buc = s3.Bucket(bucket_name)
    lis = []
    for x in test_buc.objects.filter(Prefix='kp index/'):
        lis.append(x.last_modified)
    for x in test_buc.objects.filter(Prefix='kp index/'):
        if x.last_modified == lis[-1]:
            latest_file = x.key

    return latest_file


file_data = fetch_last_modified_kp_forecast_file()

x = file_data.split()[3]
print("so this is file: ", file_data)
print("this is x: ", x)
