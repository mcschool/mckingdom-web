from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('players', meta, autoload=True)
    athletic_clear_count = Column('athletic_clear_count', Integer, default=0)
    athletic_clear_count.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('players', meta, autoload=True)
    table.c.athletic_clear_count.drop()

