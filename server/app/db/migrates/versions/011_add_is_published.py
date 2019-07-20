from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('topics', meta, autoload=True)
    role = Column('is_published', Boolean, default=False)
    role.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('topics', meta, autoload=True)
    table.c.is_published.drop()
