from sqlalchemy import Column, MetaData, Table, BigInteger, String, DateTime, Integer, Text
from migrate import *

meta = MetaData()
table = Table(
    'athletic_courses', meta,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('course_no', Integer),
    Column('name', String(255)),
    Column('description', Text),
    Column('difficulty', Integer),
    Column('updated_at', DateTime),
    Column('created_at', DateTime),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
