import json
import os

import boto3
from dotenv import load_dotenv

load_dotenv()


class FetchFileData:
    """
        takes desired file & convert into dictionary format
    """

    def __init__(self, aws_access_key_id, aws_secret_access_key):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def get_client(self):
        return boto3.client("s3", aws_access_key_id=self.aws_access_key_id,
                            aws_secret_access_key=self.aws_secret_access_key)

    def fetch_response(self, bucket_name, file_name=None):
        s3_client = FetchFileData.get_client(self)

        if not file_name:
            return ValueError('You must pass the file for conversion')

        response = s3_client.get_object(Bucket=bucket_name, Key=file_name)

        raw_data = response.get('Body')
        if not raw_data:
            raise ValueError('Response does not have \'Body\' attribute.')

        data = raw_data.read().decode('UTF-8')
        response = json.loads(data)
        return FetchFileData.format_json(response)

    @staticmethod
    def format_json(response):
        response_data = response
        top_row = response_data[0]
        total_column = len(top_row)

        formatted_data = []
        for response_row in response_data[1:]:
            formatted_data.append({top_row[col_index]: response_row[col_index]
                                   for col_index in range(total_column)})

        return formatted_data


ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

data_fetcher = FetchFileData(ACCESS_KEY, SECRET_KEY)
# result = data_fetcher.fetch_response(BUCKET_NAME, file_name='kp index/KP Forecast 2022.09.08 1702.json')


# print("So this is proton_flux: ", proton_flux)


# the second way to convert json data into dictionary file formate:
def convert_into_json(file_name):
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY)

    content_object = s3.Object(BUCKET_NAME, file_name)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    top_row = json_content[0]
    total_column = len(top_row)

    formatted_data = []
    for response_row in json_content[1:]:
        formatted_data.append({top_row[col_index]: response_row[col_index]
                               for col_index in range(total_column)})

    return formatted_data


# converted_dic = convert_into_json(file_name='kp index/KP Forecast 2022.09.08 1702.json')

def fetch_last_modified_kp_forecast_file():
    bucket_name = "swxdailyview"
    conn = boto3.session.Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    s3 = conn.resource('s3')
    bucket_data = s3.Bucket(bucket_name)
    lis = []
    for x in bucket_data.objects.filter(Prefix='kp index/'):
        lis.append(x.last_modified)
    for x in bucket_data.objects.filter(Prefix='kp index/'):
        if x.last_modified == lis[-1]:
            latest_file = x.key
            # print("yayy",type(latest_file))

    return latest_file
