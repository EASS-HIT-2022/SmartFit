from lib2to3.pgen2.token import OP
import uuid
from pydantic import BaseModel, EmailStr, Field, conint

from enum import Enum
from datetime import datetime
from typing import List, Optional

class social_(BaseModel):
    facebook: Optional[str] = '',
    twitter: Optional[str] = '',
    instagram: Optional[str] = '',
    linkedin: Optional[str] = '',
    youtube: Optional[str] = '',



class goalsEnum(str, Enum):
    get_healthy = "Get Healthy and Keep my Body in Shape"
    lose_fat = "Lose Fat"
    gain_weight = "Gain Weight"
    gain_muscle = "Gain Muscle"


class fav_splitEnum(str, Enum):
    upper_lower = "Upper Lower"
    body_part = "Body Part"
    push_pull_legs = "Push,Pull, Legs"
    full_body = "Full Body"


class ProfileBase(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(..., description="User id")


class ProfileUpdate(BaseModel):
    avatar: str = None
    height: conint(ge=100, le=300) = None
    weight: conint(ge=40, le=200) = None
    age: conint(ge=12, le=120) = None
    BMI: float = None
    is_premium: Optional[str] = False
    premium_until: Optional[str] = None
    daily_active: str = False
    health_problems_physical: List[str] = None
    diet_restrictions: List[str] = None
    fav_split: str = None
    goal: str = None
    social: social_  = {}



    class Config:
        schema_extra = {
            "example": {
                "email": "talsagie11@gmail.com",
                "avatar": "str",
                "height": 190,
                "weight": 85,
                "age": 24,
                "BMI": 110,
                "is_premium": True,
                "premium_until": datetime.now(),
                "daily_active": False,
                "health_problems_physical": ["Heart disease", "High blood pressure"],
                "diet_restrictions": ["Gluten Free", "Vegan"],
                "fav_split": fav_splitEnum.upper_lower,
                "goal": goalsEnum.gain_muscle,
                "social": {
                    "facebook": "https://www.facebook.com/talsagie",
                    "twitter": "https://twitter.com/talsagie",
                    "instagram": "https://www.instagram.com/talsagie",
                    "linkedin": "https://www.linkedin.com/in/talsagie",
                    "youtube": "https://www.youtube.com/user/talsagie"
            }

        }
        }


class ProfileCreate(ProfileUpdate):
    email: EmailStr = Field(..., description="User email")

class Profile(ProfileBase, ProfileCreate):
    class Config:
        schema_extra = {
            "example": {
                "id": "5f0f8f8f-b8f8-4f8f-8f8f-8f8f8f8f8f8f",
                "user_id": "1a09bd7c-bb7e-4382-910f-dfe6f279c55f",
                "email": "talsagie19@gmail.com",
                "avatar": "str",
                "height": 190,
                "weight": 85,
                "age": 24,
                "BMI": 110,
                "is_premium": "True",
                "premium_until": datetime.now(),
                "daily_active": False,
                "health_problems_physical": ["Heart disease", "High blood pressure"],
                "diet_restrictions": ["Gluten Free", "Vegan"],
                "fav_split": fav_splitEnum.upper_lower,
                "goal": goalsEnum.gain_muscle,
                "social": {
                    "facebook": "https://www.facebook.com/talsagie",
                    "twitter": "https://twitter.com/talsagie",
                    "instagram": "https://www.instagram.com/talsagie",
                    "linkedin": "https://www.linkedin.com/in/talsagie",
                    "youtube": "https://www.youtube.com/user/talsagie"
            }
            }
        }
