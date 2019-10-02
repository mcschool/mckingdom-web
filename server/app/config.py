# coding:utf8
import os


class BaseConfig:
    DEBUG = True


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@localhost/mckingdom"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:sbM5Jm86FG0iv4pm@35.243.117.11/mckingdom"


class LocalProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:sbM5Jm86FG0iv4pm@35.243.117.11/mckingdom"


config = {
    "local": LocalConfig,  # ローカル開発
    "local_production": LocalProductionConfig,  # ローカルから本番のDB繋ぐやつ
    "production": ProductionConfig,  # 本番
}


def configure_app(application):
    config_name = os.getenv("FLASK_CONFIGURATION", "local")
    print("@@@@@@@@@@@@@@@@@@@@")
    print("1", config_name)
    print("2", config[config_name])
    print("@@@@@@@@@@@@@@@@@@@@")
    application.config.from_object(config[config_name])
