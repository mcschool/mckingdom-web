from sqlalchemy.ext.declarative import declarative_base
from ..db import get_database_engine

class BaseModel:
    def _asdict(self):
        values = dict(
            (column.name, getattr(self, column.name))
            for column in self.__table__.columns
        )
        del_key = ['created_at', 'updated_at']
        for k in del_key:
            if values.get(k):
                del values[k]
        return values

DeclarativeBase = declarative_base(cls=BaseModel)

def init():
    engine = get_database_engine()
    DeclarativeBase.metadata.create_all(bind=engine)
