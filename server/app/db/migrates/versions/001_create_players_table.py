from sqlalchemy import Column, MetaData, Table, BigInteger, String, DateTime
from migrate import *

meta = MetaData()
table = Table(
    'players', meta,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('uuid', String(255), nullable=False),
    Column('name', String(255), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
