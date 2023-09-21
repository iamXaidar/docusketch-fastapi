from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config.settings import POSTGRES_URL
from typing import Generator

# POSTGRES sync engine and session
engine = create_engine(url=POSTGRES_URL)
local_session = sessionmaker(bind=engine, expire_on_commit=False)


# db session dependency
def get_db() -> Generator:
    db = local_session()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
