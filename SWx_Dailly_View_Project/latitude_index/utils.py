from io import StringIO

import pandas as pd

from SWx_Dailly_View_Project.constants import MID_LATITUDE_FOLDER_NAME, HIGH_LATITUDE_FOLDER_NAME
from SWx_Dailly_View_Project.s3_services import fetch_bucket_data, get_s3_client, BUCKET_NAME

bucket_data = fetch_bucket_data()


def fetch_last_modified_mid_latitude_file():
    try:
        lis = [x.last_modified for x in bucket_data.objects.filter(Prefix=MID_LATITUDE_FOLDER_NAME)]

        for x in bucket_data.objects.filter(Prefix=MID_LATITUDE_FOLDER_NAME):
            if x.last_modified == lis[-1]:
                return x.key
    except ValueError as e:
        return f"There is something wrong with file fetching {e}"


def fetch_last_modified_high_latitude_file():
    try:
        lis = [x.last_modified for x in bucket_data.objects.filter(Prefix=HIGH_LATITUDE_FOLDER_NAME)]
        for x in bucket_data.objects.filter(Prefix=HIGH_LATITUDE_FOLDER_NAME):
            if x.last_modified == lis[-1]:
                return x.key
    except ValueError as e:
        return f"There is something wrong with file fetching {e}"


def get_csv_data(file_name):
    s3_client = get_s3_client()
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
    raw_data = response.get('Body')
    data = raw_data.read().decode('UTF-8')
    return pd.read_csv(StringIO(data))


def get_g_percentage(count_for_kp):
    kp_rates = {i: count_for_kp[i] if i in count_for_kp.keys() else 0 for i in range(1, 10)}

    g_percentage = {}
    if kp_rates[5] != 0:
        g_percentage['minor'] = (kp_rates[5] / 16) * 100
    if kp_rates[6] != 0:
        g_percentage['moderate'] = (kp_rates[6] / 16) * 100
    if kp_rates[7] != 0:
        g_percentage['strong'] = (kp_rates[7] / 16) * 100
    if kp_rates[8] != 0:
        g_percentage['severe'] = (kp_rates[8] / 16) * 100
    if kp_rates[9] != 0:
        g_percentage['extreme'] = (kp_rates[9] / 16) * 100
    else:
        if not kp_rates[5]:
            g_percentage['minor'] = 0
        if not kp_rates[6]:
            g_percentage['moderate'] = 0
        if not kp_rates[7]:
            g_percentage['strong'] = 0
        if not kp_rates[8]:
            g_percentage['severe'] = 0
        if not kp_rates[9]:
            g_percentage['extreme'] = 0

    return g_percentage
