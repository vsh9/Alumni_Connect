from ninja import Schema
from pydantic import Field, EmailStr
from typing import Optional, Dict

class AlumniSchema(Schema):
    alumni_ID: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: int
    address: Optional[str] = None
    graduation_year: int
    degree: str
    major: str
    occupation: str
    company: Optional[str] = None
    linkedIn_profile: Optional[str] = None
    bio: Optional[str] = None
    
