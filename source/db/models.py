from db.database import Base
from sqlalchemy import Column, String, UUID, INT


# Create SQLAlchemy models here
class Items(Base):
    __table_name__ = "item"
    item_id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    size = Column(INT)
