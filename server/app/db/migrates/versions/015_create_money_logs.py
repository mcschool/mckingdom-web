from sqlalchemy import Column, MetaData, Table, BigInteger, String, DateTime, Integer, Text
from migrate import *

meta = MetaData()
table = Table(
    'money_logs', meta,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('uuid', String(255), nullable=False),
    Column('type', String(32), nullable=True),
    Column('money', Integer),
    Column('created_at', DateTime),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
