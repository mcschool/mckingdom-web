from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func
from ._base import DeclarativeBase


class Player(DeclarativeBase):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(255))
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    login_count = Column(Integer, default=1)
    last_login_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    pvp_max_kill_streaks = Column(Integer, default=0)
    pvp_total_kills = Column(Integer, default=0)
    role = Column(String(32))
    athletic_clear_count = Column(Integer, default=0)
    money = Column(Integer, default=0)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
