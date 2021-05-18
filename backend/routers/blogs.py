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

@router.post("/", response_model=schemas.Blog)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db=db, blog=blog)

@router.get("/{blog_id}", response_model=schemas.Blog)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    return crud.get_blog_by_id(db=db, blog_id=blog_id)

@router.patch("/{blog_id}", response_model=schemas.Blog)
def update_blog(blog: schemas.BlogUpdate, blog_id: int, db: Session = Depends(get_db)):
    return crud.update_blog(db=db, blog_id=blog_id, blog=blog)