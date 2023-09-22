"""DocuSketch FastApi Test project by Khaidar Zakirov"""
from api.items.handlers import items_router
from config.settings import DEBUG
from config.settings import logconfig
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI
from fastapi.routing import APIRouter
from fastapi.requests import Request
from middlewares import catch_exceptions_middleware
from logging.config import dictConfig
from logs.log import file_logger, LogRoute
from fastapi.responses import JSONResponse
from starlette import status
from starlette.exceptions import HTTPException as SHttpException
from tests.items.handlers import tests_router


# logging config before app starting
dictConfig(logconfig)

# Main app
app = FastAPI(debug=DEBUG, title="DocuSketchTest")
file_logger.info("Application is started...")

# Routing settings
main_router = APIRouter(route_class=LogRoute)
main_router.include_router(items_router, prefix="/items", tags=["items"])
main_router.include_router(tests_router, prefix="/tests", tags=["tests"])


@app.exception_handler(SHttpException)
async def custom_http_exception_handler(request, exc):
    """Add file logging"""
    file_logger.info(
        f"Request: {request.client.host}:{request.client.port} - {request.method} {request.url.path}{request.url.query} "
        f"Response: {exc.status_code}")
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    file_logger.info(
        f"Request: {request.client.host}:{request.client.port} - {request.method} {request.url.path}{request.url.query} "
        f"Response: 422")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@main_router.get("/")
def get_root():
    """Home page greeting message..."""
    return {"message": "Welcome to test project!"}


# Other
app.include_router(main_router)
app.middleware("http")(catch_exceptions_middleware)
