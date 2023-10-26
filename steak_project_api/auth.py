import os

from fastapi import HTTPException, Request

API_KEY: str = os.environ["API_KEY"]


async def is_authenticated(request: Request) -> bool:
    if request.state.token is None or request.state.token != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Could not authenticate",
        )

    return True
