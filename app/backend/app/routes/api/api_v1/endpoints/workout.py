from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, status, Request
from models.User import UserInDBBase
from models.Exercise import Exercise
from ..deps import get_current_active_user
from models.Workout import Workout, WorkoutCreate
from fastapi.encoders import jsonable_encoder
from db import db
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/", tags=["Workout"], description='Get my workout details')
async def my_workout(current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    if (workout := await db.get_collection("workout").find_one({"user_id": current_user.id})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=workout)
    raise HTTPException(
        status_code=404, detail="workout for current user not found")


@router.get("/{userid}", tags=["Workout"], description="Get user's workout details")
async def user_workout(userid: str) -> JSONResponse:
    if (workout := await db.get_collection("workout").find_one({"user_id": userid})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=workout)
    raise HTTPException(
        status_code=404, detail=f"workout for user {userid} not found")


@router.post("/create", tags=["Workout"], description="create a workout")
async def create_workout(workout: WorkoutCreate,current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    if (workout_ := await db.get_collection("workout").find_one({"user_id": current_user.id})) is not None:
        raise HTTPException(
            status_code=404, detail=f"workout for user {current_user.id} already exists")
    user_workout = jsonable_encoder(Workout(**workout.dict(), user_id=current_user.id))
    user_workout_res = await db.get_collection("workout").insert_one(user_workout)
    create_workout = await db.get_collection("workout").find_one(
        {"_id": user_workout_res.inserted_id}
    )
    if create_workout is not None:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=create_workout)
    raise HTTPException(
        status_code=404, detail=f"Workout couldnt be created")


@router.post("/add_exercises", tags=["Workout"], description="Add an exercise to a workout")
async def add_exrecise_to_workout(current_user: UserInDBBase = Depends(get_current_active_user), exercises: List[Exercise] = Body(...)) -> JSONResponse:
    try:
        workout = await my_workout(current_user)
    except HTTPException as e:
        raise HTTPException(
            status_code=404, detail=f"workout for current user not found")
    workout = Workout(**workout)
    workout.exrecises.extend(exercises)
    workout = jsonable_encoder(workout)
    result = await db.get_collection('workout').replace_one({'_id': workout['_id']}, workout)
    if result.modified_count == 1:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=workout)
    else:
        raise HTTPException(
            status_code=404, detail=f"workout couldnt be updated")


@router.delete("/delete_exercise", tags=["Workout"], description="delete an exercise from a workout")
async def delete_exrecise_from_workout(exercise_id: str,current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    try:
        workout = await my_workout(current_user)
    except HTTPException as e:
        raise HTTPException(
            status_code=404, detail=f"workout for current user not found")

    workout = Workout(
        **workout)
    workout.exrecises = [
        ex for ex in workout.exrecises if ex.id != exercise_id]
    workout = jsonable_encoder(workout)
    result = await db.get_collection('workout').replace_one({'_id': workout['_id']}, workout)
    if result.modified_count == 1:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=workout)
    else:
        raise HTTPException(
            status_code=404, detail=f"workout couldnt be updated")


@router.patch("/", tags=["Workout"], description="Update a workout")
async def my_workout_update(current_user: UserInDBBase = Depends(get_current_active_user), workout: WorkoutCreate = Body(...)) -> JSONResponse:
    my_work = await my_workout(current_user)
    my_stored_workout = Workout(**my_work)
    update_data = workout.dict(exclude_unset=True)
    updated_workout = my_stored_workout.copy(update=update_data)
    updated_workout = jsonable_encoder(updated_workout)

    result = await db.get_collection("workout").update_one({'_id': updated_workout['_id']}, {'$set': updated_workout})
    if result.modified_count == 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content='Workout not updated')
    workout_updated = await db.get_collection("workout").find_one({'_id': updated_workout['_id']})
    return JSONResponse(status_code=status.HTTP_200_OK, content=workout_updated)


@router.delete("/", tags=["Workout"], description="Delete my workout")
async def my_workout_delete(current_user: UserInDBBase = Depends(get_current_active_user)):
    my_workout_ = await my_workout(current_user)
    if (work := await db.get_collection("workout").find_one_and_delete({"_id": my_workout_['_id']})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=work)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='No Workout found')
