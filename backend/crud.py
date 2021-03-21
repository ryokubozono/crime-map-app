from sqlalchemy.orm import Session

from . import models, schemas

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(crime_type = event.crime_type, address = event.address, lat = event.lat, long = event.long, date=event.date)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_crimes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Crime).offset(skip).limit(limit).all()

def get_crimes_by_type(db: Session, skip: int =0, limit: int = 100, crime_type: int = 0, lat: float = 35.68 , lng: float = 139.78, zoom: int = 9):
    return db.query(models.Crime).\
        filter(models.Crime.crime_type==crime_type).\
        filter(models.Crime.fy>lat-(8.6-1.36*zoom+0.0548*zoom**2)).\
        filter(models.Crime.fy<lat+(8.6-1.36*zoom+0.0548*zoom**2)).\
        filter(models.Crime.fx>lng-(20.2-3.36*zoom+0.141*zoom**2)).\
        filter(models.Crime.fx<lng+(20.2-3.36*zoom+0.141*zoom**2)).\
        offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
