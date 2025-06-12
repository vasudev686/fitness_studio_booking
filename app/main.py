from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Studio Booking API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/classes", response_model=schemas.ClassOut)
def create_class(class_data: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db, class_data)

@app.get("/classes", response_model=list[schemas.ClassOut])
def get_classes(db: Session = Depends(get_db)):
    return crud.get_classes(db)

@app.post("/book", response_model=schemas.BookingOut)
def book_class(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    result = crud.create_booking(db, booking)
    if result is None:
        raise HTTPException(status_code=400, detail="Class not found or no slots available")
    return result

@app.get("/bookings", response_model=list[schemas.BookingOut])
def get_bookings(client_email: str, db: Session = Depends(get_db)):
    return crud.get_bookings_by_email(db, client_email)
