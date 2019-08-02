from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
import json
from ._base import DeclarativeBase


class AthleticCourse(DeclarativeBase):
    __tablename__ = 'athletic_courses'
    id = Column(Integer, primary_key=True)
    course_no = Column(Integer)
    name = Column(String(255))
    description = Column(String(255))
    image_path = Column(String(255))
    difficulty = Column(Integer)
    updated_at = Column(DateTime, default=datetime.now())
    created_at = Column(DateTime, default=datetime.now())
    play_count = Column(Integer, default=0)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
