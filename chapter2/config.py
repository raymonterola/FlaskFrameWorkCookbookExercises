import secrets


class BaseConfig:
    SECRET_KEY = secrets.token_hex()
    DEBUG = True
