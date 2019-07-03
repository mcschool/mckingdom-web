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
    login_count = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
