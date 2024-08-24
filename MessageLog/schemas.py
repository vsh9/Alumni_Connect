from datetime import datetime
from ninja import Schema

class MLCreateSchema(Schema):
    N_id: int
    delivery_status: str
    response_status: str

class MLReadSchema(Schema):
    ml_id: int
    N_id: int
    sent_at: datetime
    delivery_status: str
    response_status: str
