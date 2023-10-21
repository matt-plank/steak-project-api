from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .middleware import auth
from .routers import measurement, timing

load_dotenv()


app = FastAPI()

app.middleware("http")(auth.extract_token)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(timing.router, prefix="/timing")
app.include_router(measurement.router, prefix="/measurement")
