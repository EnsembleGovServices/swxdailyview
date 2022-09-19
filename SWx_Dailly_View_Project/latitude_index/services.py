from io import StringIO

import pandas as pd

from SWx_Dailly_View_Project.latitude_index.utils import fetch_last_modified_mid_latitude_file, \
    fetch_last_modified_high_latitude_file
from SWx_Dailly_View_Project.s3_services import get_s3_client, BUCKET_NAME


class GetMidLatitudeResource:

    @staticmethod
    def get_mid_latitude():
        s3_client = get_s3_client()
        file_name = fetch_last_modified_mid_latitude_file()
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
        raw_data = response.get('Body')
        data = raw_data.read().decode('UTF-8')
        csv_data = pd.read_csv(StringIO(data))
        print("this is csv data: ", csv_data)
        return "This is mid latitude"


class GetHighLatitudeResource:

    @staticmethod
    def get_high_latitude():
        s3_client = get_s3_client()
        file_name = fetch_last_modified_high_latitude_file()
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
        raw_data = response.get('Body')
        data = raw_data.read().decode('UTF-8')
        csv_data = pd.read_csv(StringIO(data))
        print("this is csv data: ", csv_data)
        return "This is high latitude"
