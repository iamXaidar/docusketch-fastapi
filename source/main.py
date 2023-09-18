from fastapi import FastAPI
from fastapi.routing import APIRouter
from config.settings import DEBUG

app = FastAPI(debug=DEBUG, title="DocuSketchTest")

