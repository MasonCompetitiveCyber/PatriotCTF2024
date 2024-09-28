from util import FLASK_SECRET_KEY
import os

class Config(object):
    SECRET_KEY = FLASK_SECRET_KEY
    MYSQL_HOST = os.environ.get("MYSQL_HOST", 'localhost')
    MYSQL_USER = os.environ.get("MYSQL_USER", 'user')
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
    MYSQL_DB = os.environ.get("MYSQL_DB", "door")
    FLAG = os.environ.get("FLAG", "PCTF{FAKE_FLAG}")

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True