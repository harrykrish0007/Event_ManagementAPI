from pydantic import BaseModel

class AttendeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    event_id: int