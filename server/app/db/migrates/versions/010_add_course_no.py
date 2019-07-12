from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('athletic_courses', meta, autoload=True)
    course_no = Column('course_no', Integer, default='user')
    course_no.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('athletic_courses', meta, autoload=True)
    table.c.course_no.drop()
