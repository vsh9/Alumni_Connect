from ninja import Schema
from datetime import date, time, datetime
from typing import Optional

class EventSchemaIn(Schema):
    event_id: int 
    event_name: str
    event_date_time: datetime
    location: str
    description: str
    event_type: str
    registration_deadline: date  
    rsvp_deadline: date 
    rsvp_status: bool 
    speaker_details: str = None
    event_status: str
    feedback_available: bool = None

class EventSchemaOut(Schema):
    event_id: int
    event_name: str
    event_date_time: datetime
    location: str
    event_type: str

class EveAl(Schema):
    event_id: int
    alumni_id: int