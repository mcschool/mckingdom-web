#!/usr/bin/env python
from flask import Flask
from migrate.versioning.shell import main

config = {
    "local": "config.LocalConfig",
    "test": "config.TestConfig",
    "development": "config.DevelopmentConfig",
    "production": "config.ProductionConfig",
}


def configure_app(application):
    env = 'local'
    application.config.from_object(config[env])
    application.config.from_pyfile('config.cfg', silent=True)


application = Flask(__name__)
configure_app(application)


if __name__ == '__main__':
    url = application.config['SQLALCHEMY_DATABASE_URI']
    print(url)
    main(debug='true', url=url, repository='.')
