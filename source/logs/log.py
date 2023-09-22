from fastapi.routing import APIRoute
from fastapi.requests import Request
from fastapi.responses import Response
import json
import logging
from typing import Callable


# Contains logs entities
class LogRoute(APIRoute):
    """Define custom routing class and add logging"""
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            response: Response = await original_route_handler(request)
            status_code: int = 200
            response_body = json.loads(response.body.decode("utf-8"))
            if isinstance(response_body, dict) and response_body.get("status_code"):
                status_code = response_body.get("status_code")
            # logging part
            file_logger.info(
                f"Request: {request.client.host}:{request.client.port} - {request.method} {request.url.path}{request.url.query} "
                f"Response: {status_code}")
            return response

        return custom_route_handler


file_logger = logging.getLogger("file-logger")
console_logger = logging.getLogger("console-logger")
