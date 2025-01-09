from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.event import Event
from schemas.event_schema import EventCreate, EventUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/events/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@router.put("/events/{event_id}")
def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.event_id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db_event.status = event.status
    db.commit()
    db.refresh(db_event)
    return db_event

@router.get("/events/")
def list_events(status: str = None, location: str = None, db: Session = Depends(get_db)):
    query = db.query(Event)
    if status:
        query = query.filter(Event.status == status)
    if location:
        query = query.filter(Event.location == location)
    return query.all()