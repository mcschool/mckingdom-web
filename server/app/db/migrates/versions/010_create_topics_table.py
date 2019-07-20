from sqlalchemy import Column, MetaData, Table, BigInteger, String, DateTime, Integer, Text
from migrate import *

meta = MetaData()
table = Table(
    'topics', meta,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('title', String(255), nullable=False),
    Column('body', Integer),
    Column('image_path', String(255)),
    Column('published_at', DateTime),
    Column('updated_at', DateTime),
    Column('created_at', DateTime),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
