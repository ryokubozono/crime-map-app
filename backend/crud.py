from sqlalchemy.orm import Session
import math
from . import models, schemas

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(crime_type = event.crime_type, address = event.address, lat = event.lat, long = event.long, date=event.date)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Place).offset(skip).limit(limit).all()

def get_places_with_filter(db: Session, skip: int =0, limit: int = 100, lat: float = 35.68 , lng: float = 139.78, zoom: int = 9):
    diff_x = 856 * math.exp(-0.7 * zoom)
    diff_y = 445 * math.exp(-0.7 * zoom)
    if zoom <= 9:
        return db.query(models.Place).\
            filter(models.Place.HYOSYO == 1).\
            filter(models.Place.fy>lat-diff_y).\
            filter(models.Place.fy<lat+diff_y).\
            filter(models.Place.fx>lng-diff_x).\
            filter(models.Place.fx<lng+diff_x).\
            offset(skip).limit(limit).all()    
    elif zoom <= 11 and zoom > 9:
        return db.query(models.Place).\
            filter(models.Place.HYOSYO == 2).\
            filter(models.Place.fy>lat-diff_y).\
            filter(models.Place.fy<lat+diff_y).\
            filter(models.Place.fx>lng-diff_x).\
            filter(models.Place.fx<lng+diff_x).\
            offset(skip).limit(limit).all()    
    else:
        return db.query(models.Place).\
            filter(models.Place.HYOSYO == 3).\
            filter(models.Place.fy>lat-diff_y).\
            filter(models.Place.fy<lat+diff_y).\
            filter(models.Place.fx>lng-diff_x).\
            filter(models.Place.fx<lng+diff_x).\
            offset(skip).limit(limit).all()    
        pass


def get_crimes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Crime).offset(skip).limit(limit).all()

def get_crimes_by_type(db: Session, skip: int =0, limit: int = 100, crime_type: int = 0, lat: float = 35.68 , lng: float = 139.78, zoom: int = 9):
    # diff_x = 90 - 26.5*zoom + 2.96*zoom**2 - 0.148*zoom**3 + 0.003*zoom**4
    # diff_y = 50 - 14.7*zoom + 1.64*zoom**2 - 0.082*zoom**3 + 0.002*zoom**4
    diff_x = 856 * math.exp(-0.7 * zoom)
    diff_y = 445 * math.exp(-0.7 * zoom)

    if crime_type == 2:
        if zoom <= 9:
            return db.query(models.Crime).\
                filter(models.Crime.id % 500 == 0).\
                filter(models.Crime.crime_type==crime_type).\
                offset(skip).limit(limit).all()
        elif zoom <= 12 and zoom > 9:
            return db.query(models.Crime).\
                filter(models.Crime.id % 50 == 0).\
                filter(models.Crime.crime_type==crime_type).\
                filter(models.Crime.fy>lat-diff_y).\
                filter(models.Crime.fy<lat+diff_y).\
                filter(models.Crime.fx>lng-diff_x).\
                filter(models.Crime.fx<lng+diff_x).\
                offset(skip).limit(limit).all()
        else:
            return db.query(models.Crime).\
                filter(models.Crime.id % 10 == 0).\
                filter(models.Crime.crime_type==crime_type).\
                filter(models.Crime.fy>lat-diff_y).\
                filter(models.Crime.fy<lat+diff_y).\
                filter(models.Crime.fx>lng-diff_x).\
                filter(models.Crime.fx<lng+diff_x).\
                offset(skip).limit(limit).all() 
    else:
        if zoom <= 9:
            return db.query(models.Crime).\
                filter(models.Crime.id % 100 == 0).\
                filter(models.Crime.crime_type==crime_type).\
                offset(skip).limit(limit).all()
        elif zoom <= 12 and zoom > 9:
            return db.query(models.Crime).\
                filter(models.Crime.id % 10 == 0).\
                filter(models.Crime.crime_type==crime_type).\
                filter(models.Crime.fy>lat-diff_y).\
                filter(models.Crime.fy<lat+diff_y).\
                filter(models.Crime.fx>lng-diff_x).\
                filter(models.Crime.fx<lng+diff_x).\
                offset(skip).limit(limit).all()
        else:
            return db.query(models.Crime).\
                filter(models.Crime.crime_type==crime_type).\
                filter(models.Crime.fy>lat-diff_y).\
                filter(models.Crime.fy<lat+diff_y).\
                filter(models.Crime.fx>lng-diff_x).\
                filter(models.Crime.fx<lng+diff_x).\
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
