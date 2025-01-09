from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.attendee import Attendee
from models.event import Event
from schemas.attendee_schema import AttendeeCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/attendees/")
def register_attendee(attendee: AttendeeCreate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.event_id == attendee.event_id).first()
    if not event or event.max_attendees <= len(db.query(Attendee).filter(Attendee.event_id == attendee.event_id).all()):
        raise HTTPException(status_code=400, detail="Event is full or does not exist")
    new_attendee = Attendee(**attendee.dict())
    db.add(new_attendee)
    db.commit()
    db.refresh(new_attendee)
    return new_attendee

@router.get("/attendees/{event_id}")
def list_attendees(event_id: int, db: Session = Depends(get_db)):
    attendees = db.query(Attendee).filter(Attendee.event_id == event_id).all()
    return attendees

@router.put("/attendees/checkin/{attendee_id}")
def check_in_attendee(attendee_id: int, db: Session = Depends(get_db)):
    attendee = db.query(Attendee).filter(Attendee.attendee_id == attendee_id).first()
    if not attendee:
        raise HTTPException(status_code=404, detail="Attendee not found")
    attendee.check_in_status = True
    db.commit()
    db.refresh(attendee)
    return attendee
