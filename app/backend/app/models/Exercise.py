from __future__ import annotations
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field, conlist
import uuid


class Exercise(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    alternatives: conlist(Exercise, min_items=0,
                          max_items=10, unique_items=True) = []
    favorite: Optional[bool] = False
    target_muscles: List[str] = None
    Instructions: str = None
    Execution: str = None

    class Config:
        schema_extra = {
            "example": {
                "id": "000ssf-0s0s0v0-s0v0v0a0-0s0s0s0s0-0s0s0s0s0",
                "name": "Seated Dumbbell Press",
                        "alternatives": [
                            {
                                "id": "000ssf-0s0s0v0-s0v0v0a0-0s0s0s1s0-0s0s0s0s0",
                                "name": "Bench Press",
                                "alternatives": [],
                                "favorite": False,
                                "target_muscles": ["Pecs"],
                                "Instructions": "lift the weights up and down",
                                "Execution": "lift up and down",
                            }
                        ],
                "favorite": False,
                "target_muscles": ["Pecs"],
                "Instructions": "lift the dumbbells up and down",
                "Execution": "lift the dumbbells up and down",
            }
        }
