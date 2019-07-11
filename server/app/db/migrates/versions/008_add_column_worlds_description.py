from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('worlds', meta, autoload=True)
    description = Column('description', Text, default=None)
    description.create(table)
    image_path = Column('image_path', String(2255), default=None)
    image_path.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('worlds', meta, autoload=True)
    table.c.description.drop()
    table.c.image_path.drop()
