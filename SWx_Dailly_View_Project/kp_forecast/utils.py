import json
import os
from datetime import datetime

import boto3
from dotenv import load_dotenv
from flask import current_app

from SWx_Dailly_View_Project.constants import KP_INDEX_FOLDER_NAME, ERROR_DETECTED

load_dotenv()

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")


# the second way to convert json data into dictionary file formate:
def convert_into_json(file_name):
    """
        Converts the desired json file into dictionary format
    """
    try:
        s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY)

        content_object = s3.Object(BUCKET_NAME, file_name)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        top_row = json_content[0]
        total_column = len(top_row)
        return [{top_row[col_index]: response_row[col_index] for col_index in range(total_column)} for response_row in
                json_content[1:]]
    except Exception as e:
        current_app.logger.error(ERROR_DETECTED.format(e))
        return None


def convert_timestamp_to_file_name(time_stamp):
    """
        This function will convert the timestamp into date and time : str
    """
    datetime_obj = datetime.fromtimestamp(time_stamp)
    date = str(datetime_obj.date()).replace('-', '.')
    time = str(datetime_obj).split()[1].split(":")[0] + str(datetime_obj).split()[1].split(":")[1]
    return f"{date} {time}"


def formatted_data_fetch(file_name):
    """
        This function finds the file from bucket and convert data into desired format
        for the further usage
    """
    try:
        conn = boto3.session.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        s3 = conn.resource('s3')
        bucket_data = s3.Bucket(BUCKET_NAME)
        files = [x.key for x in bucket_data.objects.filter(Prefix=KP_INDEX_FOLDER_NAME) if
                 str(x.key).split()[3] == file_name.split()[0] and str(x.key).split()[4].split(".")[0][:2] ==
                 file_name.split()[1][:2] and str(x.key).split()[4].split(".")[0] <= file_name.split()[1]]
        desired_file = files[-1]
        file_date = desired_file.split()[3]
        file_date = file_date.replace(".", "-")
        formatted_data = convert_into_json(file_name=desired_file)
        if formatted_data is None:
            return None
        return file_date, formatted_data
    except Exception as e:
        current_app.logger.error(ERROR_DETECTED.format(e))
        return None
