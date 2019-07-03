# coding:utf-8
import os
from flask import current_app
from flask_script import Manager
from app import application
from app.db import get_database_engine
from app.models._base import DeclarativeBase
from migrate.versioning.shell import main as migrate_main

manager = Manager(application)


@manager.command
def migrate(argv):
    print(os.path.dirname(os.path.abspath(__file__)))
    database_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
    migrate_main(argv=argv, debug='true', url=database_uri, repository='.db/migrates')


if __name__ == "__main__":
    manager.run()
