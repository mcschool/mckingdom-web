from sqlalchemy import Column, MetaData, Table, BigInteger, String, DateTime, Integer
from migrate import *

meta = MetaData()
table = Table(
    'players', meta,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('uuid', String(255), nullable=False),
    Column('name', String(255), nullable=False),
    Column('password', String(255)),
    Column('login_count', Integer, default=0),
    Column('last_login_at', DateTime),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
