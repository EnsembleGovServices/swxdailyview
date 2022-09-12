import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EXPIRE_TIME_FOR_ACCESS_TOKEN_IN_MINUTES = int(os.getenv('EXPIRE_TIME_FOR_ACCESS_TOKEN_IN_MINUTES'))
    EXPIRE_TIME_FOR_REFRESH_TOKEN_IN_HOURS = int(os.getenv('EXPIRE_TIME_FOR_REFRESH_TOKEN_IN_HOURS'))
    EXPIRE_TIME_FOR_FORGOT_PASSWORD_TOKEN_IN_MINUTES = int(
        os.getenv('EXPIRE_TIME_FOR_FORGOT_PASSWORD_TOKEN_IN_MINUTES'))
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


class Development(BaseConfig):
    """
    Development environment configuration
    """
    DEBUG = True
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


app_config = {
    'development': Development,
}
