from sqlalchemy.orm import Session
from . import models, schemas

def create_class(db: Session, class_data: schemas.ClassCreate):
    new_class = models.FitnessClass(**class_data.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

def get_classes(db: Session):
    return db.query(models.FitnessClass).filter(models.FitnessClass.availableSlots > 0).all()

def create_booking(db: Session, booking: schemas.BookingCreate):
    class_obj = db.query(models.FitnessClass).filter_by(id=booking.class_id).first()
    if not class_obj or class_obj.availableSlots <= 0:
        return None
    class_obj.availableSlots -= 1
    new_booking = models.Booking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

def get_bookings_by_email(db: Session, email: str):
    return db.query(models.Booking).filter(models.Booking.client_email == email).all()
