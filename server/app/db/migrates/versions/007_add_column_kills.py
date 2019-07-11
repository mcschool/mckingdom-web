from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('players', meta, autoload=True)
    pvp_max_kill_streaks = Column('pvp_max_kill_streaks', Integer, default=0)
    pvp_max_kill_streaks.create(table)
    pvp_total_kills = Column('pvp_total_kills', Integer, default=0)
    pvp_total_kills.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('players', meta, autoload=True)
    table.c.pvp_max_kill_streaks.drop()
    table.c.pvp_total_kills.drop()
