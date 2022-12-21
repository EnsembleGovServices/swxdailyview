import os
import time
from datetime import date, timedelta

import pytest
from dotenv import load_dotenv
from SWx_Dailly_View_Project import create_app

load_dotenv()


@pytest.fixture()
def app():
    app = create_app(env_name=os.getenv('TEST_ENV'))
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope='module')
def access_data():
    access_key = os.getenv('ACCESS_KEY')
    secret_key = os.getenv('SECRET_KEY')
    bucket_name = os.getenv('BUCKET_NAME')

    return access_key, secret_key, bucket_name


current_date = date.today()
last_one_day = current_date - timedelta(days=1)

tuple = last_one_day.timetuple()
last_date_timestamp = int(str(time.mktime(tuple)).split('.')[0])
desired_time_stamps = []
desired_time_stamps.append(last_date_timestamp)
for i in range(23):
    desired_time_stamps.append(last_date_timestamp+3600)
    last_date_timestamp+=3600
@pytest.fixture()
def time_stamp():
    time_stamp_value = desired_time_stamps[0]
    return time_stamp_value

@pytest.fixture()
def time_stamp_13hour():
    time_stamp_value = desired_time_stamps[13]
    return time_stamp_value

@pytest.fixture()
def time_stamp_12hour():
    time_stamp_value = desired_time_stamps[12]
    return time_stamp_value
@pytest.fixture()
def time_stamp_10hour():
    time_stamp_value = desired_time_stamps[10]
    return time_stamp_value
@pytest.fixture()
def time_stamp_11hour():
    time_stamp_value = desired_time_stamps[11]
    return time_stamp_value

@pytest.fixture()
def time_stamp_9hour():
    time_stamp_value = desired_time_stamps[9]
    return time_stamp_value

@pytest.fixture()
def time_stamp_8hour():
    time_stamp_value = desired_time_stamps[8]
    return time_stamp_value

@pytest.fixture()
def time_stamp_7hour():
    time_stamp_value = desired_time_stamps[7]
    return time_stamp_value

@pytest.fixture()
def time_stamp_6hour():
    time_stamp_value = desired_time_stamps[6]
    return time_stamp_value

@pytest.fixture()
def time_stamp_5hour():
    time_stamp_value = desired_time_stamps[5]
    return time_stamp_value

@pytest.fixture()
def time_stamp_4hour():
    time_stamp_value = desired_time_stamps[4]
    return time_stamp_value

@pytest.fixture()
def time_stamp_3hour():
    time_stamp_value = desired_time_stamps[3]
    return time_stamp_value

@pytest.fixture()
def time_stamp_2hour():
    time_stamp_value = desired_time_stamps[2]
    return time_stamp_value

@pytest.fixture()
def time_stamp_1hour():
    time_stamp_value = desired_time_stamps[1]
    return time_stamp_value

@pytest.fixture()
def time_stamp_0hour():
    time_stamp_value = desired_time_stamps[0]
    return time_stamp_value

@pytest.fixture()
def time_stamp_14hour():
    time_stamp_value = desired_time_stamps[14]
    return time_stamp_value

@pytest.fixture()
def time_stamp_15hour():
    time_stamp_value = desired_time_stamps[15]
    return time_stamp_value

@pytest.fixture()
def time_stamp_16hour():
    time_stamp_value = desired_time_stamps[16]
    return time_stamp_value

@pytest.fixture()
def time_stamp_17hour():
    time_stamp_value = desired_time_stamps[17]
    return time_stamp_value

@pytest.fixture()
def time_stamp_18hour():
    time_stamp_value = desired_time_stamps[18]
    return time_stamp_value

@pytest.fixture()
def time_stamp_19hour():
    time_stamp_value = desired_time_stamps[19]
    return time_stamp_value

@pytest.fixture()
def time_stamp_20hour():
    time_stamp_value = desired_time_stamps[20]
    return time_stamp_value

@pytest.fixture()
def time_stamp_21hour():
    time_stamp_value = desired_time_stamps[21]
    return time_stamp_value

@pytest.fixture()
def time_stamp_22hour():
    time_stamp_value = desired_time_stamps[22]
    return time_stamp_value

@pytest.fixture()
def time_stamp_23hour():
    time_stamp_value = desired_time_stamps[23]
    return time_stamp_value

time_list = [ time_stamp, time_stamp_0hour, time_stamp_1hour,
              time_stamp_2hour, time_stamp_3hour, time_stamp_4hour,
              time_stamp_5hour, time_stamp_6hour, time_stamp_7hour,
              time_stamp_8hour, time_stamp_9hour, time_stamp_10hour,
              time_stamp_11hour,time_stamp_12hour, time_stamp_13hour,
              time_stamp_14hour, time_stamp_15hour, time_stamp_16hour,
              time_stamp_17hour, time_stamp_18hour, time_stamp_19hour,
              time_stamp_20hour, time_stamp_21hour, time_stamp_22hour,
              time_stamp_23hour]