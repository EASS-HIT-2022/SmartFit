from typing import List
import uuid
from pydantic import BaseModel, EmailStr, Field
from models.Exercise import Exercise


class WorkoutBase(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(..., description="User id")


class WorkoutCreate(BaseModel):
    number_of_days_per_week: int = Field(default=3)
    exercises: List[Exercise] = Field(default=[])

    class Config:
        schema_extra = {
            "number_of_days_per_week": "3",
            "exercises": [
                {
                    "id": "000ssf-0s0s0v0-s0v0v0a0-0s0s0s0s0-0s0s0s0s0",
                    "name": "Seated Dumbbell Press",
                    "alternatives": [
                            {
                                "id": "000ssf-0s0s0v0-s0v0v0a0-0s0s0s1s0-0s0s0s0s0",
                                "name": "Bench Press",
                                "alternatives": [''],
                                "favorite": False,
                                "target_muscles": "Pecs",
                                "Instructions": "lift the weights up and down",
                                "Execution": "lift up and down",
                            }
                    ],
                    "favorite": False,
                    "target_muscles": "Pecs",
                    "Instructions": "lift the dumbbells up and down",
                    "Execution": "lift the dumbbells up and down",
                }
            ],
        }


class Workout(WorkoutBase, WorkoutCreate):

    class Config:
        schema_extra = {
            "example": {
                "id": '000ssf-0s0s0v0-s0v0v0a0-0s0s0s0s0-0s0s0s0s0',
                'user_id': '1a09bd7c-bb7e-4382-910f-dfe6f279c55f',
                "number_of_days_per_week": "3",
                "exercises": [
                    {
                        "id": "000ssf-0s0s0v0-s0v0v0a0-0s0s0s0s0-0s0s0s0s0",
                        "name": "Seated Dumbbell Press",
                        "alternatives": [
                            {
                                "id": "000ssf-0s0s0v0-s0v0v0a0-0s0s0s1s0-0s0s0s0s0",
                                "name": "Bench Press",
                                "alternatives": [''],
                                "favorite": False,
                                "target_muscles": "Pecs",
                                "Instructions": "lift the weights up and down",
                                "Execution": "lift up and down",
                            }
                        ],
                        "favorite": False,
                        "target_muscles": "Pecs",
                        "Instructions": "lift the dumbbells up and down",
                        "Execution": "lift the dumbbells up and down",
                    }
                ],

            }
        }
