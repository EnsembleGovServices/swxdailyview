import os

from dotenv import load_dotenv

from SWx_Dailly_View_Project import create_app

load_dotenv()

env_name = os.getenv('FLASK_ENV')

application = create_app(env_name=env_name)

if __name__ == '__main__':
    application.run(debug=True)
