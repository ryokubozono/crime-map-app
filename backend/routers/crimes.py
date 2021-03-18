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

@router.get("/", response_model=List[schemas.Crime])
def read_crimes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    crimes = crud.get_crimes(db, skip=skip, limit=limit)
    return crimes

@router.get("/{crime_type}", response_model=List[schemas.Crime])
def get_crimes_by_type(crime_type: int, skip: int = 0, limit: int = 100, lat: float = 35.68, lng: float = 139.78, db: Session = Depends(get_db)):
    crimes = crud.get_crimes_by_type(db, skip=skip, limit=limit, crime_type=crime_type, lat=lat, lng=lng)

    return crimes
