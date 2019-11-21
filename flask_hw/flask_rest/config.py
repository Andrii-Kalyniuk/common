import os


class Config:
    DEBUG = False
    PG_USER = 'cursor'
    PG_PASSWORD = 'very_secret_password'
    PG_HOST = 'localhost'
    PG_PORT = '5432'
    DB_NAME = 'test_orm'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DEBUG = True
    PG_USER = 'cursor'
    PG_PASSWORD = 'very_secret_password'
    PG_HOST = 'localhost'
    PG_PORT = '5432'
    DB_NAME = 'hotel_rest_orm'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProdConfig(Config):
    pass


def get_config(env=None):
    if not env:
        env = os.environ.get("ENV")
    if env == "TEST":
        return TestConfig
    elif env == "PROD":
        return ProdConfig
    else:
        return Config
