from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from ._base import DeclarativeBase


class Player(DeclarativeBase):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(255))
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    login_count = Column(Integer, default=1)
    last_login_at = Column(DateTime, default=datetime.now())
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
