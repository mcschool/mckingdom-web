from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from ._base import DeclarativeBase


class Player(DeclarativeBase):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
