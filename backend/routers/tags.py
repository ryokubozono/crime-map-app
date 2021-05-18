from fastapi import APIRouter, Header, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import SessionLocal, engine

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    return crud.create_tag(db=db, tag=tag)

@router.get("/{tag_id}", response_model=schemas.Tag)
def get_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
    return crud.get_tag_by_id(db=db, tag_id=tag_id)

@router.get("/", response_model=List[schemas.Tag])
def get_tags(db: Session = Depends(get_db)):
    return crud.get_tags(db=db)

@router.patch("/{tag_id}", response_model=schemas.Tag)
def update_tag(tag_id: int, tag: schemas.TagUpdate, db: Session = Depends(get_db)):
    return crud.update_tag(db=db, tag=tag, tag_id=tag_id)