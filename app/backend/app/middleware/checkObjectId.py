from typing import Callable
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        response = await call_next(request)

        return response


# # each request will be passed to this middleware
# # i want the id of each request will be checked if it is valid or not
