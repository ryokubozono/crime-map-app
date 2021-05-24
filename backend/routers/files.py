from fastapi import APIRouter, Header, HTTPException, Depends, File, UploadFile
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import SessionLocal, engine
import shutil
import os
import rstr
from ..auth import get_user

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@router.post("/uploadfile/")
async def create_upload_file(image: UploadFile = File(...), user = Depends(get_user)):
    dir, ext = os.path.splitext(image.filename)
    new_filename = rstr.xeger(r'^[0-9]{2}[0-9a-zA-Z0-9]{10}') + ext
    upload_path = f"uploads/{new_filename}"
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {"filename": new_filename, "filepath": "/" + upload_path}