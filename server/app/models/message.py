from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, Text
from ._base import DeclarativeBase


class Message(DeclarativeBase):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    world = Column(String(255))
    message = Column(Text)
    updated_at = Column(DateTime, default=datetime.now())
    created_at = Column(DateTime, default=datetime.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
