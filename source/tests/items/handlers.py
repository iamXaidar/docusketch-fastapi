from tests.items.dependencies import get_test_db
from typing import Annotated
from sqlalchemy.orm import Session
from db.crud import ItemCRUD
from fastapi import APIRouter, Depends, Body, Path
from api.items import schemas

tests_router = APIRouter()


# Test endpoints handlers to work with test db
@tests_router.post("/items", response_model=schemas.ShowItem)
def create_item(item: Annotated[schemas.CreateItem, Body()],
                db: Session = Depends(get_test_db)
                ) -> schemas.ShowItem:
    crud = ItemCRUD(db)
    db_item = crud.create_item(item)
    return schemas.ShowItem(
        id=db_item.id,
        name=db_item.name
    )


@tests_router.get("/")
def get_test_message():
    return {"message": "Test endpoint works"}


@tests_router.get("/")
def get_test_message():
    return {"message": "Test endpoint works"}
