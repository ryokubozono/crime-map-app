from typing import List
from starlette.requests import Request
from fastapi import Depends, FastAPI, HTTPException
from starlette.responses import RedirectResponse, JSONResponse, HTMLResponse
from starlette.staticfiles import StaticFiles
from .routers import events
from .routers import users
from .routers import crimes 
from starlette.middleware.cors import CORSMiddleware

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/dist"), name="static")
app.include_router(events.router, prefix="/api/events")
app.include_router(crimes.router, prefix="/api/crimes")
app.include_router(users.router, prefix="/api/users")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)