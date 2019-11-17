import json
from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func
from ._base import DeclarativeBase


class World(DeclarativeBase):
    __tablename__ = 'worlds'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    login_count = Column(Integer)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, default=func.now())
    description = Column(String(255))
    image_path = Column(String(255))
    world_name = Column(String(64))
    server_name = Column(String(64))


    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
