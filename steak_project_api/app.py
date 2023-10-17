from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import measurement, timing

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(timing.router, prefix="/timing")
app.include_router(measurement.router, prefix="/measurement")
