from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
import json
from ._base import DeclarativeBase


class AthleticCompletedPlayers(DeclarativeBase):
    __tablename__ = 'athletic_completed_players'
    id = Column(Integer, primary_key=True)
    athletic_course_id = Column(Integer)
    player_id = Column(String(255))
    player_uuid = Column(String(255))
    total_time = Column(Integer)
    updated_at = Column(DateTime, default=datetime.now())
    created_at = Column(DateTime, default=datetime.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
