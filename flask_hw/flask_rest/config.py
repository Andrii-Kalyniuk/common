import os


class Config:
    DEBUG = False


class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


def run_config():
    env = os.environ.get("ENV")
    if env == "TEST":
        return TestConfig
    elif env == "PROD":
        return ProdConfig
    else:
        return Config
