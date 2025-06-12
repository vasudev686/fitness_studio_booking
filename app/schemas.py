from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClassCreate(BaseModel):
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

class ClassOut(ClassCreate):
    id: int

    class Config:
       form_attributes = True


class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BookingCreate):
    id: int

    class Config:
        orm_mode = True
