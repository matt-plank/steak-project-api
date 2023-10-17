import os

from fastapi import Request
from fastapi.responses import JSONResponse

API_KEY: str = os.environ["API_KEY"]


def requires_key(func):
    async def wrapper(request: Request):
        if request.state.token is None:
            return JSONResponse(
                content={"message": "Authorization required"},
                status_code=401,
            )

        if request.state.token != API_KEY:
            return JSONResponse(
                content={"message": "Invalid API key"},
                status_code=401,
            )

        return await func(request)

    return wrapper
