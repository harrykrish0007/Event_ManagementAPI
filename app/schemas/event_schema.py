from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str
    max_attendees: int

class EventUpdate(BaseModel):
    status: str