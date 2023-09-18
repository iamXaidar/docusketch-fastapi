from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import POSTGRES_URL

engine = create_engine(url=POSTGRES_URL)
local_session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

# SQLAlchemy base model
Base = declarative_base()
