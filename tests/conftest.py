import os

import pytest
from dotenv import load_dotenv

from SWx_Dailly_View_Project import create_app

load_dotenv()
env_name = os.getenv('TEST_ENV')


@pytest.fixture
def client():
    app = create_app(env_name=env_name)
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


def test_status(client):
    res = client.get('/')
    assert res.status_code == 200


def test_current_kp(client):
    res = client.get('/current-kp-index')
    assert res.status_code == 200


def test_get_interval_kp(client):
    res = client.get('/get-interval-kp-data')
    assert res.status_code == 200


def test_predicted_kp(client):
    res = client.get('/predicted-kp-index')
    assert res.status_code == 200


def test_get_proton_flux(client):
    res = client.get('/get-proton-flux-data')
    assert res.status_code == 200


def test_get_mid_latitude(client):
    res = client.get('/get-mid-latitude')
    assert res.status_code == 200


def test_get_high_latitude(client):
    res = client.get('/get-high-latitude')
    assert res.status_code == 200
