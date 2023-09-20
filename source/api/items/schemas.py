from pydantic import BaseModel
from db.models import Item
from typing import List, Type


# Create pydantic models here
class OrmModeMixin(BaseModel):
    """Allow to use orm syntax"""
    class Config:
        from_attributes = True


class CreateItem(OrmModeMixin):
    name: str


class ShowItem(OrmModeMixin):
    item_id: int
    name: str


class ShowItems(OrmModeMixin):
    items: List[Type[ShowItem]]


class UpdateItem(OrmModeMixin):
    name: str
