
from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import Optional

class PatientCreate(BaseModel):
    name: str = Field(min_length= 1, max_length= 100)
    age : int = Field(ge= 0, le= 120)
    condition: str = Field(min_length = 1)
    risk_score: int = Field(ge = 0, le = 100)
    active: bool = True 

class Patient(SQLModel, table = True):
    id : Optional[int] = Field(default=None, primary_key = True)
    name: str = Field(min_length= 1, max_length= 100)
    age : int = Field(ge= 0, le= 120)
    condition: str = Field(min_length = 1)
    risk_score: int = Field(ge = 0, le = 100)
    active: bool = True 

class PatientUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    age: Optional[int] = Field(default=None, ge=0, le=120)
    condition: Optional[str] = Field(default=None, min_length=1)
    risk_score: Optional[int] = Field(default=None, ge=0, le=100)
    active: Optional[bool] = None

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    hashed_password: str

class UserRead(BaseModel):
    id: int
    username: str

class UserCreate(BaseModel):
    username: str
    password: str