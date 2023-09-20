from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config.settings import POSTGRES_URL
from typing import Generator

# POSTGRES sync engine
engine = create_engine(url=POSTGRES_URL)
local_session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


# db dependency
def get_db() -> Generator:
    db = local_session()
    try:
        yield db
    finally:
        db.close()
