from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('players', meta, autoload=True)
    money = Column('money', Integer, default=0)
    money.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('players', meta, autoload=True)
    table.c.money.drop()

