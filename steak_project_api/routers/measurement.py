from fastapi import APIRouter, Depends

from .. import schemas
from ..auth import is_authenticated
from ..db import measurements

router = APIRouter()


@router.get("/", response_model=list[schemas.Measurement])
async def get():
    """View all the stored measurements."""
    all_measurements = [
        schemas.Measurement(
            id=str(measurement["_id"]),
            thickness=measurement["thickness"],
            cookTime=measurement["cookTime"],
            doneness=measurement["doneness"],
        )
        for measurement in measurements.find()
    ]

    return all_measurements


@router.post("/", response_model=schemas.Measurement, status_code=201)
async def create(measurement: schemas.NewMeasurement, auth: bool = Depends(is_authenticated)):
    """Create a new measurement and store it."""
    inserted = measurements.insert_one(measurement.model_dump())

    result = schemas.Measurement(
        **measurement.model_dump(),
        id=str(inserted.inserted_id),
    )

    return result
