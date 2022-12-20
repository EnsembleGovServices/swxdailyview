import os
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


@pytest.fixture()
def time_stamp():
    time_stamp_value = 1671527941
    return time_stamp_value

@pytest.fixture()
def time_stamp_13hour():
    time_stamp_value = 1671521825
    return time_stamp_value

@pytest.fixture()
def time_stamp_12hour():
    time_stamp_value = 1671518225
    return time_stamp_value
@pytest.fixture()
def time_stamp_10hour():
    time_stamp_value = 1671511025
    return time_stamp_value
@pytest.fixture()
def time_stamp_11hour():
    time_stamp_value = 1671514625
    return time_stamp_value

@pytest.fixture()
def time_stamp_9hour():
    time_stamp_value = 1671507425
    return time_stamp_value

@pytest.fixture()
def time_stamp_8hour():
    time_stamp_value = 1671503825
    return time_stamp_value

@pytest.fixture()
def time_stamp_7hour():
    time_stamp_value = 1671500225
    return time_stamp_value

@pytest.fixture()
def time_stamp_6hour():
    time_stamp_value = 1671496625
    return time_stamp_value

@pytest.fixture()
def time_stamp_5hour():
    time_stamp_value = 1671493025
    return time_stamp_value

@pytest.fixture()
def time_stamp_4hour():
    time_stamp_value = 1671489425
    return time_stamp_value

@pytest.fixture()
def time_stamp_3hour():
    time_stamp_value = 1671485825
    return time_stamp_value

@pytest.fixture()
def time_stamp_2hour():
    time_stamp_value = 1671482225
    return time_stamp_value

@pytest.fixture()
def time_stamp_1hour():
    time_stamp_value = 1671478625
    return time_stamp_value

@pytest.fixture()
def time_stamp_0hour():
    time_stamp_value = 1671475025
    return time_stamp_value

@pytest.fixture()
def time_stamp_14hour():
    time_stamp_value = 1671525425
    return time_stamp_value

@pytest.fixture()
def time_stamp_15hour():
    time_stamp_value = 1671529025
    return time_stamp_value

@pytest.fixture()
def time_stamp_16hour():
    time_stamp_value = 1671532625
    return time_stamp_value

@pytest.fixture()
def time_stamp_17hour():
    time_stamp_value = 1671536225
    return time_stamp_value

@pytest.fixture()
def time_stamp_18hour():
    time_stamp_value = 1671539825
    return time_stamp_value

@pytest.fixture()
def time_stamp_19hour():
    time_stamp_value = 1671543425
    return time_stamp_value

@pytest.fixture()
def time_stamp_20hour():
    time_stamp_value = 1671547025
    return time_stamp_value

@pytest.fixture()
def time_stamp_21hour():
    time_stamp_value = 1671550625
    return time_stamp_value

@pytest.fixture()
def time_stamp_22hour():
    time_stamp_value = 1671554225
    return time_stamp_value

@pytest.fixture()
def time_stamp_23hour():
    time_stamp_value = 1671557793
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