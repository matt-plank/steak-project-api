import pymongo
from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter

from .. import auth, db, schemas

router = APIRouter()


@router.get("/{doneness}", response_model=schemas.Model)
def get(doneness: str):
    model = db.models.find_one({"doneness": doneness}, sort=[("created", pymongo.DESCENDING)])

    if model is None:
        raise HTTPException(
            status_code=404,
            detail=f"No model for doneness {doneness!r}",
        )

    response = schemas.Model(
        id=str(model["_id"]),
        coefficients=model["coefficients"],
        created=model["created"],
        doneness=model["doneness"],
    )

    return response


@router.post("/", status_code=201)
def post(model: schemas.NewModel, auth=Depends(auth.is_authenticated)):
    inserted = db.models.insert_one(model.model_dump())

    return schemas.Model(
        **model.model_dump(),
        id=str(inserted.inserted_id),
    )
