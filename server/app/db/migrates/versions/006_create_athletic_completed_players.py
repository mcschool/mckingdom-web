from sqlalchemy import Column, MetaData, Table, BigInteger, String, DateTime, Integer, Text
from migrate import *

meta = MetaData()
table = Table(
    'athletic_completed_players', meta,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('athletic_course_id', Integer),
    Column('player_id', String(255)),
    Column('player_uuid', String(255)),
    Column('total_time', Integer),
    Column('updated_at', DateTime),
    Column('created_at', DateTime),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
