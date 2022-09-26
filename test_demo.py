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
    rv = client.get('/')
    assert rv.status_code == 200