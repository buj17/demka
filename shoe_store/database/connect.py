import sqlalchemy.orm
from sqlalchemy.orm import Session

from config import settings

engine = sqlalchemy.create_engine(settings.DATABASE_URL)

SessionLocal = sqlalchemy.orm.sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def create_session() -> Session:
    return SessionLocal()
