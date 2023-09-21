from api.items import schemas
from db import models
from sqlalchemy.orm import Session
from typing import List, Type


class ItemCRUD:
    """Class that implements crud and other actions"""
    def __init__(self, db: Session):
        self.db = db

    def create_item(self, item: schemas.CreateItem) -> models.Item:
        db_item = models.Item(name=item.name)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def get_items(self, offset: int = 0, limit: int = 25) -> List[Type[models.Item]]:
        items = self.db.query(models.Item).order_by("id").offset(offset).limit(limit).all()
        return items

    def detail_item(self, item_id: int) -> models.Item:
        return self.db.query(models.Item).get(item_id)
        # return self.db.query(models.Item).filter(models.Item.item_id == item_id).first()  # ?

    def update_item(self, item_id: int, item: schemas.UpdateItem) -> models.Item:
        db_item = self.db.query(models.Item).get(item_id)

        if db_item.name is not None:
            db_item.name = item.name
            self.db.commit()
        return db_item

    def delete_items(self, items: schemas.DeleteItems):
        items = set(items.ids)
        rows = self.db.query(models.Item).filter(models.Item.id.in_(items)).delete()
        self.db.commit()
        return {"deleted rows count": rows,
                "deleted item ids": items
                }
