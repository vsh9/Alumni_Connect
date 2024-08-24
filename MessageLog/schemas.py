from datetime import datetime
from ninja import Schema

class MLCreateSchema(Schema):
    n_id: int
    delivery_status: str
    response_status: str

class MLReadSchema(Schema):
    ml_id: int
    n_id: int
    sent_at: datetime
    delivery_status: str
    response_status: str
