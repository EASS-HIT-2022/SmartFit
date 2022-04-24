from __future__ import annotations
import datetime
from email.policy import default
import uuid
from pydantic import BaseModel, Field, conlist
from models.Food import Food
from typing import List


class MenuBase(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(..., description="User id")


class MenuUpdate(MenuBase):
    foods: conlist(
        Food, min_items=0, max_items=100, unique_items=True) = []


class Menu(MenuUpdate):
    total_calories: int = 0
    calories_from_fat: float = 0
    calories_from_protien: float = 0
    calories_from_carbs: float = 0
    time_created: datetime.datetime = None

    class Config:
        schema_extra = {
            "example": {
                'id: 1a09xbd7c-bdb7e-a4382-91a0f-dfe6f279c55f'
                'user_id': '1a09bd7c-bb7e-4382-910f-dfe6f279c55f',
                "total_calories": 0,
                "calories_from_fat": 0,
                "calories_from_protien": 0,
                "calories_from_carbs": 0,
                "time_created": datetime.datetime.now(),
                "foods": [
                    {
                        "id": "apple-130",
                        "name": "apple",
                        "grams": 130,
                        "type": "fruit",
                        "calories": 132,
                        "fat": 9.5,
                        "carbs": 27,
                        "protein": 3,
                        "sodium": 11,
                        "fiber": 20,
                        "sugar": 20,
                        "cholesterol": 50,
                        "saturated_fat": 3,
                        "alternatives": [],
                    },

                ]
            }
        }
