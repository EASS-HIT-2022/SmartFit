from __future__ import annotations
import uuid
from typing import List
from pydantic import UUID4, BaseModel, Field, conlist


class Food(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    grams: float = Field(...)
    type: str = Field(...)
    calories: float = Field(...)
    fat: float = Field(...)
    carbs: float = Field(...)
    protein: float = Field(...)
    sodium: float = 0
    fiber: float = 0
    sugar: float = 0
    cholesterol: float = 0
    saturated_fat: float = 0
    alternatives: conlist(item_type=Food, min_items=0,
                          max_items=10, unique_items=True)

    class Config:
        schema_extra = {
            "example": {
                "id": "de5a8a99-f86f-46ec-9185-e71a00c7d1da",
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

            }
        }
