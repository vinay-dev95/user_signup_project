from pydantic import BaseModel, EmailStr, validator
from sqlalchemy import Column, Integer, String
from database import Base

# class UserSignup(BaseModel):
#     name: str
#     email: EmailStr
#     password: str

# SqlAlchemy Model

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str
    
    @validator("email")
    def validate_email(cls, v):
        if not v.endswith("@gmail.com"):
            raise ValueError("only gmail address are allowed.")
        return v
    
    @validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        return v
        

class Userlogin(BaseModel):
    email: EmailStr
    password: str
    