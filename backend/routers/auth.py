from fastapi import APIRouter, Header, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import SessionLocal, engine
from ..auth import get_user
router = APIRouter()

@router.get("/")
async def hello():
    return {"msg":"Hello, this is API server"}

@router.get("/me/")
async def hello_user(user = Depends(get_user)):
    return {"msg":"Hello, user","uid":user['uid']}