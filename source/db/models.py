from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import Identity
from sqlalchemy import Column, String, Integer


# Create SQLAlchemy models here
# SQLAlchemy base model
class Base(DeclarativeBase):
    pass


class Item(Base):
    """The simplest models"""
    __tablename__ = "item"
    item_id: Mapped[int] = mapped_column(Integer, Identity(start=1, cycle=True), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)

