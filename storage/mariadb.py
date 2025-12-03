from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from models.mariadb_models import Base

DATABASE_URL = "mysql+mysqlconnector://root:ahmed123@localhost:3306/assignment07"

engine: Engine = create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def init_db() -> None:
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)


@contextmanager
def get_session() -> Generator[Session, None, None]:
    """Provide a transactional scope around a series of operations."""
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
