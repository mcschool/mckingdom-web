from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, Text, Boolean
from ._base import DeclarativeBase


class Topic(DeclarativeBase):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    body = Column(Text)
    image_path = Column(String(255))
    published_at = Column(DateTime, default=None)
    updated_at = Column(DateTime, default=datetime.now())
    created_at = Column(DateTime, default=datetime.now())
    is_published = Column(Boolean, default=False)


    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
