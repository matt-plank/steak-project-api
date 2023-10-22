from fastapi import Request
from fastapi.responses import JSONResponse


def header_is_valid(header: str) -> bool:
    if not header.startswith("Bearer "):
        return False

    return True


async def extract_token(request: Request, call_next):
    request.state.token = None

    if "Authorization" not in request.headers:
        return await call_next(request)

    AUTHORIZATION_HEADER: str = request.headers["Authorization"]

    if not header_is_valid(AUTHORIZATION_HEADER):
        return JSONResponse(
            content={"message": "Improperly formatted Authorization header"},
            status_code=401,
        )

    TOKEN: str = AUTHORIZATION_HEADER[7:]

    request.state.token = TOKEN

    return await call_next(request)
