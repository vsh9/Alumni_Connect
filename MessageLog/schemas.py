from datetime import datetime
from ninja import Schema

class MLCreateSchema(Schema):
    n_id: int
    alumni_id: int
    message: str
    sent_at: datetime
    response_status: str

class MLReadSchema(Schema):
    ml_id: int
    n_id: int
    alumni_id: int
    message: int
    sent_at: datetime
    delivery_status: str
    response_status: str
