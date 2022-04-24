from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel, EmailStr, Field, constr


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: constr(max_length=128) = None

    class Config:
        json_encoders = {datetime: str}
        schema_extra = {
            "example": {
                "email": "talsagie19@gmail.com",
                "full_name": 'Tal Sagie',
                "password": "mypassword"
            }
        }


class UserUpdate(UserBase):
    new_password_hashed: Optional[str] = None


class UserInDBBase(UserBase):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    password_hash: constr(max_length=128) = None
    disabled: bool = False
    create_date: datetime = None

    class Config:
        json_encoders = {datetime: str}
        schema_extra = {
            "example": {
                "email": "talsagie19@gmail.com",
                "full_name": 'Tal Sagie',
                "id": '1a09bd7c-bb7e-4382-910f-dfe6f279c55f',
                "create_date": datetime.now(),
                "password": "$#R#$#$T#$%$%^%$Y^&"
            }
        }
