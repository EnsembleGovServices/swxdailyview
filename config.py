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


class Testing(BaseConfig):
    """
    Production environment configuration
    """
    TESTING = True


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}

