from fastapi import FastAPI

from .routers import timing

app = FastAPI()
app.include_router(timing.router, prefix="/timing")
