import os

import logging


class Config:
    DEBUG = False


class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


def get_config(env=None):
    if not env:
        env = os.environ.get("ENV")
    logging.info(env)
    config_options = {
        "TEST": TestConfig,
        "PROD": ProdConfig
    }
    return config_options.get(env, Config)
