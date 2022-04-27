from __future__ import annotations
from email.policy import default
import uuid
from typing import List
from pydantic import UUID4, BaseModel, Field, conlist


class Food(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(..., description="Name of the food")
    grams: float = Field(..., description="Grams of the food")
    type: str = Field(..., description="Type of the food")
    calories: float = Field(..., description="Calories of the food")
    fat: float = Field(..., description="Fat of the food")
    carbs: float = Field(..., description="Carbs of the food")
    protein: float = Field(..., description="Protein of the food")
    sodium: float = 0
    fiber: float = 0
    sugar: float = 0
    cholesterol: float = 0
    saturated_fat: float = 0
    alternatives: conlist(item_type=Food, min_items=0,
                          max_items=10, unique_items=True) = []

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
