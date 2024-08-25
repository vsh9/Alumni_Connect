from ninja import Schema
from typing import Optional


class NTFSchemaIn(Schema):
    n_id: int
    event_id: int
    n_type: str
    n_content: str
    priority: Optional[str]

class NTFSchemaOut(Schema):
    n_id: int
    n_type: str
    n_content: str