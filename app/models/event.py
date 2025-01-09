from sqlalchemy import Column, Integer, String, DateTime, Enum
from database import Base

class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String)
    max_attendees = Column(Integer)
    status = Column(Enum('scheduled', 'ongoing', 'completed', 'canceled'), default='scheduled')
