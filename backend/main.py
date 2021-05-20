from typing import List
from starlette.requests import Request
from fastapi import Depends, FastAPI, HTTPException
from starlette.responses import RedirectResponse, JSONResponse, HTMLResponse
from starlette.staticfiles import StaticFiles
from .routers import events
from .routers import users
from .routers import crimes 
from .routers import places
from .routers import blogs
from .routers import tags
from .routers import files
from .routers import auth
from starlette.middleware.cors import CORSMiddleware

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/dist"), name="static")
app.include_router(events.router, prefix="/api/events", tags=["events"])
app.include_router(crimes.router, prefix="/api/crimes", tags=["crimes"])
app.include_router(places.router, prefix="/api/places", tags=["places"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(blogs.router, prefix="/api/blogs", tags=["blogs"])
app.include_router(tags.router, prefix="/api/tags", tags=["tags"])
app.include_router(files.router, prefix="/api/files", tags=["files"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)