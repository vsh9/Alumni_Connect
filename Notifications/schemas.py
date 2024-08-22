from ninja import Schema
from pydantic import Field, EmailStr
from typing import Optional, Dict
from Events.schemas import EventSchema 


class NTFSchemaIn(Schema):
    N_id: int
    event_id: int
    N_type: str
    N_content: str
    Priority: Optional[str]

class NTFSchemaOut(Schema):
    N_id: int
    N_type: str
    N_content: str