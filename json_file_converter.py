from dotenv import load_dotenv

load_dotenv()
import os

import boto3
import json

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")


def convert_into_json(file_name):
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY)

    content_object = s3.Object('swxdailyview', file_name)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    top_row = json_content[0]
    total_column = len(top_row)

    formatted_data = []
    for response_row in json_content[1:]:
        formatted_data.append({top_row[col_index]: response_row[col_index]
                               for col_index in range(total_column)})

    return formatted_data
