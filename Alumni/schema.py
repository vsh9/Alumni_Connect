from ninja import Schema
from pydantic import Field, EmailStr
from typing import Optional, Dict

class AlumniSchema(Schema):
    Alumni_ID: int
    First_Name: str
    Last_Name: str
    Email: EmailStr
    Phone_Number: int
    Address: Optional[str] = None
    Graduation_Year: int
    Degree: str
    Major: str
    Occupation: str
    Company: Optional[str] = None
    LinkedIn_Profile: Optional[str] = None
    Bio: Optional[str] = None
    
