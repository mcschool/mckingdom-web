from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('athletic_courses', meta, autoload=True)
    money = Column('play_count', Integer, default=0)
    money.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('athletic_courses', meta, autoload=True)
    table.c.play_count.drop()

