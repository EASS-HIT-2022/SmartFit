
from typing import List
from fastapi import APIRouter, HTTPException
from models.Exercise import Exercise
from db import db

router = APIRouter()


@router.get("/api/api_v1/exercises/{id}", tags=["Exercise"], response_description='Get speseific exrecise details')
async def get_exrecise(id: str):
    if (ex := await db.get_collection("exercises").find_one({"_id": id})) is not None:
        return ex
    raise HTTPException(status_code=404, detail=f"Exercise {id} not found")


@router.get("/api/api_v1/exercises", tags=["Exercise"], response_model=List[Exercise], response_description='Get all exrecises details')
async def get_all_exrecise():
    exercises_list = []
    for ex in await db.get_collection("exercises").find().to_list(length=100):
        exercises_list.append(ex)
    if len(exercises_list) > 0:
        return exercises_list
    else:
        raise HTTPException(status_code=404, detail=f"No exercises found")
