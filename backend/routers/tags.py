from fastapi import APIRouter, Header, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import SessionLocal, engine
from ..auth import get_user

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_tag/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db), user = Depends(get_user)):
    return crud.create_tag(db=db, tag=tag)

@router.get("/all/", response_model=List[schemas.Tag])
def get_tags_all(db: Session = Depends(get_db), user = Depends(get_user)):
    return crud.get_tags_all(db=db)

@router.get("/visible/", response_model=List[schemas.Tag])
def get_tags_visible(db: Session = Depends(get_db)):
    return crud.get_tags_visible(db=db)

@router.get("/get_tag/{tag_id}/", response_model=schemas.Tag)
def get_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
    return crud.get_tag_by_id(db=db, tag_id=tag_id)

@router.patch("/update_tag/{tag_id}/", response_model=schemas.Tag)
def update_tag(tag_id: int, tag: schemas.TagUpdate, db: Session = Depends(get_db), user = Depends(get_user)):
    return crud.update_tag(db=db, tag=tag, tag_id=tag_id)