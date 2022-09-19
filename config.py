class BaseConfig:
    pass


class Development(BaseConfig):
    """
    Development environment configuration
    """
    DEBUG = True


class Production(BaseConfig):
    """
    Production environment configuration
    """
    DEBUG = False


app_config = {
    'development': Development,
    'production': Production
}
