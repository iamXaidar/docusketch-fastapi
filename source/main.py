"""DocuSketch FastApi Test project by Khaidar Zakirov"""
from api.items.handlers import items_router
from fastapi import FastAPI
from fastapi.routing import APIRouter
from config.settings import DEBUG

# Main app and routing settings
app = FastAPI(debug=DEBUG, title="DocuSketchTest")
main_router = APIRouter()
main_router.include_router(items_router, prefix="/items", tags=["item"])
app.include_router(main_router)


@app.get("/")
def get_root():
    """Home page greeting message..."""
    return {"message": "Welcome to test project!"}


