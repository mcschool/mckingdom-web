from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from ._base import DeclarativeBase


class MoneyLog(DeclarativeBase):
    __tablename__ = 'money_logs'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(255))
    type = Column(String(32))  # 払ったか、もらったか ... use or get
    money = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
