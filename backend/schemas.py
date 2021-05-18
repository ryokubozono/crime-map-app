from typing import List, Optional
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel

class BlogBase(BaseModel):
    content: str
    title: str
    image_url: str

class BlogCreate(BlogBase):
    tags: List[int]

class BlogUpdate(BlogBase):
    tags: List[int]

class BlogInDB(BlogBase):
    id: int

    class Config:
        orm_mode = True

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagUpdate(TagBase):
    pass

class TagInDB(TagBase):
    id: int

    class Config:
        orm_mode = True 

class Tag(TagInDB):
    blogs: List[BlogInDB]

class Blog(BlogInDB):
    tags: List[TagInDB]
    created_at: datetime
    updated_at: datetime

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

class EventBase(BaseModel):
    crime_type: int
    lat: float
    long: float
    date: date
    address: str
    created_at: datetime
    updated_at: datetime

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True

class EventCreate(EventBase):
    id: int

########## Crime
class CrimeBase(BaseModel):
    pass

class Crime(CrimeBase):
    id: int
    crime_type: int
    
    class Config:
        orm_mode = True
    
    police_area: Optional[str] = None
    police_city: Optional[str] = None
    city_code: Optional[float] = None
    prefecture: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    date: Optional[str] = None
    hour: Optional[str] = None
    location: Optional[str] = None

    key: Optional[str] = None
    anti_theft: Optional[str] = None
    object: Optional[str] = None
    location_name: Optional[str] = None
    fx: Optional[float] = None
    fy: Optional[float] = None
    iconf: Optional[float] = None
    ilvl: Optional[float] = None
    gender: Optional[str] = None
    age: Optional[str] = None
    job: Optional[str] = None
    money: Optional[str] = None

########## Place
class PlaceBase(BaseModel):
    pass

class Place(PlaceBase):
    id: int

    class Config:
        orm_mode = True
    
    KEY_CODE: Optional[int] = None
    HYOSYO: Optional[int] = None
    ITYNAME: Optional[str] = None
    PLACENAME: Optional[str] = None
    HTKSYORI: Optional[int] = None
    HTKSAKI: Optional[int] = None
    GASSAN: Optional[int] = None
    population: Optional[int] = None
    men: Optional[int] = None
    women: Optional[int] = None
    homes: Optional[int] = None
    LocName: Optional[str] = None
    fx: Optional[float] = None
    fy: Optional[float] = None
    iconf: Optional[int] = None
    ilvl: Optional[int] = None
    crime_0: Optional[int] = None
    crime_1: Optional[int] = None
    crime_2: Optional[int] = None
    crime_3: Optional[int] = None
    crime_4: Optional[int] = None
    crime_5: Optional[int] = None
    crime_6: Optional[int] = None
