from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/")
async def create(request: Request):
    json_data = await request.json()

    if "thickness" not in json_data:
        return JSONResponse(
            status_code=400,
            content={"message": "You must provide a thickness"},
        )

    thickness: float = json_data["thickness"]

    return {
        "rare": 30 * thickness,
        "midRare": 40 * thickness,
        "medium": 50 * thickness,
        "midWell": 60 * thickness,
        "well": 70 * thickness,
    }
