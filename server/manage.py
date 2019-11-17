# coding:utf-8
import os
import glob
from flask import current_app
from flask_script import Manager
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_seed import load_fixtures, load_fixture_files
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


@manager.command
def import_data():
    print("start import data")
    session_maker = sessionmaker(autocommit=False, autoflush=False, bind=get_database_engine())
    session = scoped_session(session_maker)
    path = os.path.join(application.root_path, 'fixtures')
    files = [os.path.split(f)[1] for f in glob.glob("./app/fixtures/*")]
    print(files)
    fixtures = load_fixture_files(path, files)
    load_fixtures(session, fixtures)
    print("finish import data")


if __name__ == "__main__":
    manager.run()
