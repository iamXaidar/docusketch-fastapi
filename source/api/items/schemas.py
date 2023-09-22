from pydantic import BaseModel, ConfigDict
from typing import List, Type


# Create pydantic models here
class OrmModeMixin(BaseModel):
    """Allow to use orm syntax"""
    model_config = ConfigDict(from_attributes=True)

    # Deprecated?
    # class Config:
    #     from_attributes = True


class CreateItem(OrmModeMixin):
    name: str


class DeleteItems(OrmModeMixin):
    ids: List[int]


class ShowItem(OrmModeMixin):
    id: int
    name: str


class ShowItems(OrmModeMixin):
    items: List[Type[ShowItem]]


class UpdateItem(OrmModeMixin):
    name: str
