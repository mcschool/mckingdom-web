from sqlalchemy import Column, MetaData, Table, BigInteger, String, DateTime, Integer
from migrate import *

meta = MetaData()
table = Table(
    'accesses', meta,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('uuid', String(255), nullable=False),
    Column('created_at', DateTime),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
