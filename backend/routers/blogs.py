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
@router.get("/all/", response_model=List[schemas.Blog])
def get_blog_all(db: Session = Depends(get_db)):
    return crud.get_blogs_all(db=db)

@router.get("/visible/", response_model=List[schemas.Blog])
def get_blog_visible(db: Session = Depends(get_db)):
    return crud.get_blogs_visible(db=db)

@router.post("/create_blog/", response_model=schemas.Blog)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db), user = Depends(get_user)):
    return crud.create_blog(db=db, blog=blog)

@router.get("/get_blog/{blog_id}/", response_model=schemas.Blog)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    return crud.get_blog_by_id(db=db, blog_id=blog_id)

@router.patch("/update_blog/{blog_id}/", response_model=schemas.Blog)
def update_blog(blog: schemas.BlogUpdate, blog_id: int, db: Session = Depends(get_db), user = Depends(get_user)):
    return crud.update_blog(db=db, blog_id=blog_id, blog=blog)