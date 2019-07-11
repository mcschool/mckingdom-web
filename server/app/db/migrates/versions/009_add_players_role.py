from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('players', meta, autoload=True)
    role = Column('role', String(32), default='user')
    role.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('players', meta, autoload=True)
    table.c.role.drop()
