from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('athletic_courses', meta, autoload=True)
    image_path = Column('image_path', String(255), default=False)
    image_path.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('athletic_courses', meta, autoload=True)
    table.c.image_path.drop()
