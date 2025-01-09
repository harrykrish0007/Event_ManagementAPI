from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base

class Attendee(Base):
    __tablename__ = "attendees"

    attendee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String)
    event_id = Column(Integer, ForeignKey('events.event_id'))
    check_in_status = Column(Boolean, default=False)