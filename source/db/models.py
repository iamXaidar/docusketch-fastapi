from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, String, Integer


# Create SQLAlchemy models here
# SQLAlchemy base model
class Base(DeclarativeBase):
    pass


class Item(Base):
    """The simplest models"""
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)

