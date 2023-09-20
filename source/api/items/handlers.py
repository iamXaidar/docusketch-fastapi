from api.items import schemas
from db.crud import ItemCRUD
from db.database import get_db
from fastapi import Depends, Path, Body, Query
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import Annotated

# Items endpoint routing
items_router = APIRouter()


@items_router.post("/", response_model=schemas.ShowItem)
def create_item(item: Annotated[schemas.CreateItem, Body()],
                db: Session = Depends(get_db)
                ) -> schemas.ShowItem:
    crud = ItemCRUD(db)
    db_item = crud.create_item(item)
    return schemas.ShowItem(
        item_id=db_item.item_id,
        name=db_item.name
    )


@items_router.get("/")
def get_items(offset: Annotated[int, Query()] = 0,
              limit: Annotated[int, Query()] = 25,
              db: Session = Depends(get_db)):
    crud = ItemCRUD(db)
    items = crud.get_items(offset, limit)
    return items


@items_router.get("/{item_id}")
def detail_item(
        item_id: Annotated[int, Path(title="The ID of the item to get")],
        db: Session = Depends(get_db)
):
    crud = ItemCRUD(db)
    return crud.detail_item(item_id)


@items_router.put("/{item_id}")
def update_item(
        item: Annotated[schemas.UpdateItem, Body()],
        item_id: Annotated[int, Path()],
        db: Session = Depends(get_db)
):
    crud = ItemCRUD(db)
    return crud.update_item(item_id=item_id, item=item)


@items_router.delete("/{item_id}")
def delete_item(
        item_id: Annotated[int, Path()],
        db: Session = Depends(get_db)
):
    crud = ItemCRUD(db)
    return crud.delete_item(item_id)

