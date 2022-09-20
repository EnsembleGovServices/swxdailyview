import os

from dotenv import load_dotenv
from flask_cors import CORS

from SWx_Dailly_View_Project import create_app

load_dotenv()

env_name = os.getenv('FLASK_ENV')

application = create_app(env_name=env_name)

CORS(application, origins=[
    "http://localhost",
    "http://localhost:*",
    "http://127.0.0.1:*",
    "http://0.0.0.0:*",
    "http://swxbackenddev-env.eba-qddq4zxt.us-east-1.elasticbeanstalk.com"
])

if __name__ == '__main__':
    application.run(debug=True)
