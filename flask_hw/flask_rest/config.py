import os


class TestConfig:
    DEBUG = True


class ProdConfig:
    DEBUG = False


def run_config():
    env = os.environ.get("ENV")
    if env == "TEST":
        return TestConfig
    else:
        return ProdConfig
