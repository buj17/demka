import sqlalchemy.orm
from sqlalchemy.orm import Session

from config import settings
from database import models

engine = sqlalchemy.create_engine(settings.DATABASE_URL)

models.Base.metadata.create_all(engine)

SessionLocal = sqlalchemy.orm.sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def create_session() -> Session:
    return SessionLocal()
