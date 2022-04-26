from typing import List
from fastapi import APIRouter, HTTPException, status
from models.Exercise import Exercise
from db import db
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/{id}", tags=["Exercise"], description='Get speseific exrecise details')
async def get_exrecise(id: str) -> JSONResponse:
    if (ex := await db.get_collection("exercises").find_one({"_id": id})) is not None:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=ex)
    raise HTTPException(status_code=404, detail=f"Exercise {id} not found")


@router.get("/", tags=["Exercise"], response_model=List[Exercise], response_description='Get all exrecises details')
async def get_all_exrecise() ->JSONResponse:
    exercises_list = []
    for ex in await db.get_collection("exercises").find().to_list(length=100):
        exercises_list.append(ex)
    if len(exercises_list) > 0:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=exercises_list)
    else:
        raise HTTPException(status_code=404, detail="No exercises found")
