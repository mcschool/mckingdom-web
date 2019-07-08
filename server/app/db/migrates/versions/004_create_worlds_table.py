from sqlalchemy import Column, MetaData, Table, BigInteger, String, DateTime, Integer, Text
from migrate import *

meta = MetaData()
table = Table(
    'worlds', meta,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('name', String(255), nullable=False),
    Column('login_count', Integer),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
