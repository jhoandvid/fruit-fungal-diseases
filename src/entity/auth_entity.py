from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=16, description="Password of user")


class UserLogin(UserBase):
    class Config:
        schema_extra = {
            "example": {
                "email": 'user@gmail.com',
                "password": 'mysecret'
            }
        }


class User(UserLogin):
    name: str = Field(description="Name user")
    role: str = Field(default="user")
    createdAt: datetime = Field(default=datetime.utcnow());

    class Config:
        schema_extra = {
            "example": {
                "email": 'user@gmail.com',
                "name": "user password",
                "password": "mysecretPAssword"
            }
        }
