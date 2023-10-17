import os

from fastapi import Request
from fastapi.responses import JSONResponse


def requires_key(func):
    async def wrapper(request: Request):
        if "API_KEY" not in os.environ:
            raise Exception("API_KEY environment variable is required")

        if "Authorization" not in request.headers:
            return JSONResponse(
                content={"message": "Authorization required"},
                status_code=401,
            )

        API_KEY: str = os.environ["API_KEY"]
        AUTHORIZATION_HEADER: str = request.headers["Authorization"]
        TOKEN: str = AUTHORIZATION_HEADER.split(" ")[1]

        if TOKEN != API_KEY:
            return JSONResponse(
                content={"message": "Invalid API key"},
                status_code=401,
            )

        return await func(request)

    return wrapper
