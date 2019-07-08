from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
import json
from ._base import DeclarativeBase


class World(DeclarativeBase):
    __tablename__ = 'worlds'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    login_count = Column(Integer)
    updated_at = Column(DateTime, default=datetime.now())
    created_at = Column(DateTime, default=datetime.now())


    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
