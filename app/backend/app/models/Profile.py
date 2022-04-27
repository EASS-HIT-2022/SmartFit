import uuid
from pydantic import BaseModel, EmailStr, Field, conint
from enum import Enum
from datetime import datetime
from typing import List, Optional


class goalsEnum(str, Enum):
    get_healthy = 'Get Healthy and Keep my Body in Shape'
    lose_fat = 'Lose Fat'
    gain_weight = 'Gain Weight'
    gain_muscle = 'Gain Muscle'


class fav_splitEnum(str, Enum):
    upper_lower = 'Upper and Lower'
    ab = 'AB'
    abc = 'ABC'
    full_body = 'Full Body'


class ProfileBase(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(..., description="User id")


class ProfileCreate(BaseModel):
    email: EmailStr = Field(..., description="User email")
    avatar: str = None
    height: conint(ge=100, le=300)
    weight: conint(ge=40, le=200)
    age: conint(ge=12, le=120)
    BMI: float = None
    is_premium: Optional[bool] = False
    premium_until: datetime = None
    daily_active: bool = False
    health_problems_physical: List[str] = None
    diet_restrictions: List[str] = None
    fav_split: fav_splitEnum = None
    goal: goalsEnum = None

    class Config:
        schema_extra = {
            "example": {
                'email': 'talsagie19@gmail.com',
                'avatar': 'str',
                'height': 190,
                'weight': 85,
                'age': 24,
                'BMI': 110,
                'is_premium': True,
                'premium_until': datetime.now(),
                'daily_active': False,
                'health_problems_physical': ['Heart disease', 'High blood pressure'],
                'diet_restrictions': ['Gluten Free', 'Vegan'],
                'fav_split': fav_splitEnum.upper_lower,
                'goal': goalsEnum.gain_muscle
            }

        }


class Profile(ProfileBase, ProfileCreate):
    class Config:
        schema_extra = {
            "example": {
                'id': '5f0f8f8f-b8f8-4f8f-8f8f-8f8f8f8f8f8f',
                'user_id': '1a09bd7c-bb7e-4382-910f-dfe6f279c55f',
                'email': 'talsagie19@gmail.com',
                'avatar': 'str',
                'height': 190,
                'weight': 85,
                'age': 24,
                'BMI': 110,
                'is_premium': 'True',
                'premium_until': datetime.now(),
                'daily_active': False,
                'health_problems_physical': ['Heart disease', 'High blood pressure'],
                'diet_restrictions': ['Gluten Free', 'Vegan'],
                'fav_split': fav_splitEnum.upper_lower,
                'goal': goalsEnum.gain_muscle
            }
        }
