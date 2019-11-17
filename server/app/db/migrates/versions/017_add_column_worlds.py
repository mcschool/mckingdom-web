from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('worlds', meta, autoload=True)
    world_name = Column('world_name', String(64))
    world_name.create(table)
    server_name = Column('server_name', String(64))
    server_name.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('worlds', meta, autoload=True)
    table.c.server_name()
    table.c.world_name()
