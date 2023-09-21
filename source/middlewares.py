from logs.log import file_logger, console_logger
from starlette.requests import Request
from starlette.responses import Response


async def catch_exceptions_middleware(request: Request, call_next):
    """Catch and log global exceptions..."""
    try:
        return await call_next(request)
    except Exception:
        file_logger.error(
            f"Request: {request.client.host}:{request.client.port} - {request.method} {request.url.path} "
            f"Response: 500\n", exc_info=True)
        console_logger.error(msg="", exc_info=True)

        return Response("Internal server error", status_code=500)
