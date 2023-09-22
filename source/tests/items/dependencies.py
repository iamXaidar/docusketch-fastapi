from config.settings import TEST_POSTGRES_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

test_engine = create_engine(url=TEST_POSTGRES_URL)
test_session = sessionmaker(bind=test_engine, expire_on_commit=False)


# test db session dependency
def get_test_db() -> Generator:
    db = test_session()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
