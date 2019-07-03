import sqlalchemy
from flask import current_app


def get_database_engine():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/mckingdom'  # current_app.config['SQLALCHEMY_DATABASE_URI']
    DEBUG = current_app.config['DEBUG']
    return sqlalchemy.create_engine(
        SQLALCHEMY_DATABASE_URI,
        echo=True,
        pool_size=10,
        max_overflow=0,
        pool_timeout=5,
    )
