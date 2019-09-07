# coding:utf8
import os


class BaseConfig:
    DEBUG = True


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/mckingdom"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@db/mckingdom"


class LocalProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@34.85.76.41/mckingdom"


config = {
    "local": LocalConfig,  # ローカル開発
    "local_production": LocalProductionConfig,  # ローカルから本番のDB繋ぐやつ
    "production": ProductionConfig,  # 本番
}


def configure_app(application):
    config_name = os.getenv("FLASK_CONFIGURATION", "local")
    print("@@@@@@@@@@@@@@@@@@@@")
    print(config_name)
    print(config[config_name])
    print("@@@@@@@@@@@@@@@@@@@@")
    application.config.from_object(config[config_name])
