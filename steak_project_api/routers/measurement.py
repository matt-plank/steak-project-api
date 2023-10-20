from dataclasses import dataclass
from enum import Enum, auto

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..auth import requires_key
from ..db import client, measurements

router = APIRouter()


class Doneness(Enum):
    RAW = auto()
    RARE = auto()
    MID_RARE = auto()
    MEDIUM = auto()
    MID_WELL = auto()
    WELL = auto()
    BURNT = auto()


@router.get("/")
async def get(request: Request) -> JSONResponse:
    """View all the stored measurements."""
    response = measurements.find()

    return JSONResponse(
        status_code=200,
        content=[
            {
                "thickness": measurement["thickness"],
                "cookTime": measurement["cookTime"],
                "doneness": measurement["doneness"],
            }
            for measurement in response
        ],
    )


@router.post("/")
@requires_key
async def create(request: Request):
    """Create a new measurement and store it."""
    request_json: dict = await request.json()

    if "thickness" not in request_json:
        return JSONResponse(
            status_code=400,
            content={"message": "thickness is required"},
        )

    if "cookTime" not in request_json:
        return JSONResponse(
            status_code=400,
            content={"message": "cookTime is required"},
        )

    if "doneness" not in request_json:
        return JSONResponse(
            status_code=400,
            content={"message": "doneness is required"},
        )

    if request_json["doneness"] not in Doneness.__members__:
        return JSONResponse(
            status_code=400,
            content={"message": f"{request_json['doneness']} is not a valid Doneness"},
        )

    measurement = {
        "thickness": request_json["thickness"],
        "cookTime": request_json["cookTime"],
        "doneness": request_json["doneness"],
    }

    measurements.insert_one(measurement)

    return JSONResponse(
        status_code=201,
        content={
            "thickness": measurement["thickness"],
            "cookTime": measurement["cookTime"],
            "doneness": measurement["doneness"],
        },
    )
