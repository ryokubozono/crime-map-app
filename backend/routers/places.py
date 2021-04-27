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

@router.get("/", response_model=List[schemas.Place])
def get_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_places(db, skip=skip, limit=limit)
    return places

@router.get("/city", response_model=List[schemas.Place])
def get_places_with_city(prefecture: str = '/', skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_places_city(db, skip=skip, limit=limit, prefecture=prefecture)
    return places

@router.get("/town", response_model=List[schemas.Place])
def get_places_with_city(prefecture: str = '/', skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_places_town(db, skip=skip, limit=limit, prefecture=prefecture)
    return places

@router.get("/street", response_model=List[schemas.Place])
def get_places_with_city(prefecture: str = '/', skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_places_street(db, skip=skip, limit=limit, prefecture=prefecture)
    return places

@router.get("/filter", response_model=List[schemas.Place])
def get_places_with_filter(skip: int = 0, limit: int = 100, lat: float = 35.68, lng: float = 139.78, zoom: int = 9, db: Session = Depends(get_db)):
    places = crud.get_places_with_filter(db, skip=skip, limit=limit, lat=lat, lng=lng, zoom=zoom)
    return places
