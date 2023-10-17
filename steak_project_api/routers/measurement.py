from dataclasses import dataclass
from enum import Enum, auto

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..auth import requires_key

router = APIRouter()


class Doneness(Enum):
    RAW = auto()
    RARE = auto()
    MID_RARE = auto()
    MEDIUM = auto()
    MID_WELL = auto()
    WELL = auto()
    BURNT = auto()


@dataclass
class Measurement:
    thickness: float
    cook_time: float
    doneness: Doneness


measurements: list[Measurement] = []


@router.post("/")
@requires_key
async def create(request: Request):
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

    measurement = Measurement(
        thickness=request_json["thickness"],
        cook_time=request_json["cookTime"],
        doneness=Doneness[request_json["doneness"]],
    )
    measurements.append(measurement)

    return {
        "thickness": measurement.thickness,
        "cookTime": measurement.cook_time,
        "doneness": measurement.doneness.name,
    }
