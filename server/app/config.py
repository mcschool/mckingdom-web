# coding:utf8
class BaseConfig:
    DEBUG = True


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@127.0.0.1/mckingdom"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@34.85.72.174/mckingdom"
