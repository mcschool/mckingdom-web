from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from ._base import DeclarativeBase


class Accesses(DeclarativeBase):
    __tablename__ = 'accesses'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
