#!/usr/bin/env python
import os
from flask import Flask
from migrate.versioning.shell import main
from config import LocalProductionConfig, LocalConfig, ProductionConfig

config = {
    "local": LocalConfig,
    "local_production": LocalProductionConfig,
    "production": ProductionConfig,
}


def configure_app(application):
    env = os.getenv('FLASK_CONFIGURATION', 'local')
    application.config.from_object(config[env])
    application.config.from_pyfile('config.cfg', silent=True)


application = Flask(__name__)
configure_app(application)


if __name__ == '__main__':
    env = os.getenv('FLASK_CONFIGURATION', 'local')
    url = application.config['SQLALCHEMY_DATABASE_URI']

    print("=================")
    print(env)
    print(url)
    print("=================")
    main(debug='true', url=url, repository='.')
