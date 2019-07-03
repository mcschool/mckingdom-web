# coding:utf8
class BaseConfig:
    DEBUG = True


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/mckingdom"
