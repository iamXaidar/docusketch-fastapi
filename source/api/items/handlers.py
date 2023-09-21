from api.items import schemas
from db.crud import ItemCRUD
from db.database import get_db
from fastapi import Depends, Path, Body, Query, HTTPException
from fastapi.requests import Request
from fastapi.routing import APIRouter
from logs.log import LogRoute, file_logger
from sqlalchemy.orm import Session
from typing import Annotated


# /items endpoint routing
items_router = APIRouter(route_class=LogRoute)


@items_router.post("/", response_model=schemas.ShowItem)
def create_item(item: Annotated[schemas.CreateItem, Body()],
                db: Session = Depends(get_db)
                ) -> schemas.ShowItem:
    crud = ItemCRUD(db)
    db_item = crud.create_item(item)
    return schemas.ShowItem(
        id=db_item.id,
        name=db_item.name
    )


@items_router.get("/")
def get_items(
        request: Request,
        offset: Annotated[int, Query()] = 0,
        limit: Annotated[int, Query()] = 25,
        db: Session = Depends(get_db)
):
    crud = ItemCRUD(db)

    items = crud.get_items(offset, limit)
    if not items:
        return HTTPException(status_code=404, detail="Requested items do not exist...")
    return items


@items_router.get("/{item_id}")
def detail_item(
        request: Request,
        item_id: Annotated[int, Path(title="The ID of the item to get")],
        db: Session = Depends(get_db)
):
    crud = ItemCRUD(db)
    item = crud.detail_item(item_id)
    if item is None:
        return HTTPException(status_code=404, detail="Requested object does not exists...")
    return item


@items_router.put("/{item_id}")
def update_item(
        item: Annotated[schemas.UpdateItem, Body()],
        item_id: Annotated[int, Path()],
        db: Session = Depends(get_db)
):
    crud = ItemCRUD(db)
    item = crud.update_item(item_id=item_id, item=item)
    if item is None:
        return HTTPException(status_code=404, detail="Requested object does not exists...")
    return item


@items_router.delete("/")
def delete_items(
        items: Annotated[schemas.DeleteItems, Body()],
        db: Session = Depends(get_db)
):
    crud = ItemCRUD(db)
    return crud.delete_items(items)

