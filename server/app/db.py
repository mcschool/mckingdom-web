import os
import sqlalchemy
from flask import current_app
from pprint import pprint as p


def get_database_engine():
    print("*******************")
    p(current_app.config)
    print("*******************")
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@db/mckingdom'  # current_app.config['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_DATABASE_URI = current_app.config['SQLALCHEMY_DATABASE_URI']
    DEBUG = current_app.config['DEBUG']
    return sqlalchemy.create_engine(
        SQLALCHEMY_DATABASE_URI,
        echo=True,
        pool_size=10,
        max_overflow=0,
        pool_timeout=5,
    )
