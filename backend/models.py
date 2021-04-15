from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval, String
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    crime_type = Column(Integer)
    address = Column(String)
    lat = Column(Float)
    long = Column(Float)
    date = Column(
        Date,
        default=func.now()
        )
    created_at = Column(
        DateTime,
        server_default=func.now()
        )
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
        )

class Crime(Base):
    __tablename__ = "crimes"
    
    id = Column(Integer, primary_key=True, index=True)
    crime_type = Column(Integer)

    police_area = Column(String)
    police_city = Column(String)
    city_code = Column(Float)
    prefecture = Column(String)
    city = Column(String)
    street = Column(String)
    date = Column(String)
    hour = Column(String)
    location = Column(String)
    
    key = Column(String)
    anti_theft = Column(String)
    object = Column(String)
    location_name = Column(String)
    fx = Column(Float)
    fy = Column(Float)
    iconf = Column(Float)
    ilvl = Column(Float)
    gender = Column(String)
    age = Column(String)
    job = Column(String)
    money = Column(String)

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)

    KEY_CODE = Column(Integer)
    HYOSYO = Column(Integer)
    CITYNAME = Column(String)
    PLACENAME = Column(String)
    HTKSYORI = Column(Integer)
    HTKSAKI = Column(Integer)
    GASSAN = Column(Integer)
    population = Column(Integer)
    men = Column(Integer)
    women = Column(Integer)
    homes = Column(Integer)
    LocName = Column(String)
    fx = Column(Float)
    fy = Column(Float)
    iconf = Column(Integer)
    ilvl = Column(Integer)
    crime_0 = Column(Integer)
    crime_1 = Column(Integer)
    crime_2 = Column(Integer)
    crime_3 = Column(Integer)
    crime_4 = Column(Integer)
    crime_5 = Column(Integer)
    crime_6 = Column(Integer)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")