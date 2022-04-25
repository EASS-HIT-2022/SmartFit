from fastapi import APIRouter, Body, HTTPException, status
from models.Food import Food
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from db import db
router = APIRouter()


@router.get("/api/api_v1/nutrition", tags=["Food"], description='Get all food details')
async def get_all_food() -> JSONResponse:
    food_list = []
    for food in await db.get_collection("food").find().to_list(length=100):
        food_list.append(food)
    if len(food_list) > 0:
        return JSONResponse(status_code=status.HTTP_200_OK, content=food_list)
    else:
        raise HTTPException(status_code=404, detail=f"No food found")


@router.get("/api/api_v1/nutrition/food/{id}", tags=["Food"], description='Get spesific food details', response_model=Food)
async def get_spesific_food(id: str) -> JSONResponse:
    if (food := await db.get_collection("food").find_one({"_id": id})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=food)
    raise HTTPException(status_code=404, detail=f"food {id} not found")


@router.post("/api/api_v1/nutrition/food/new", tags=["Food"], description='When one user wants to add a spesific food which isnt in the database')
async def post_one_food(food: Food = Body(...)) -> JSONResponse:
    food_data = jsonable_encoder(food)
    new_food_data = await db.get_collection("food").insert_one(food_data)
    created_food = await db.get_collection("food").find_one(
        {"_id": new_food_data.inserted_id}
    )
    if created_food is not None:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_food)
    raise HTTPException(
        status_code=404, detail=f"Food {food.id} couldnt be created")


# @router.delete("/api/api_v1/nutrition/food/{id}", tags=["Food"], description='delete food')
# async def del_food(id: str):
#     if (food := await db.get_collection("food").find_one({"_id": id})) is not None:
#         await db.get_collection("food").delete_one({"_id": id})
#         return HTTPException(
#             status_code=201, detail=f"food {id} deleted")
#     raise HTTPException(
#         status_code=404, detail=f"food {id} not found")
#
# thinking about deleting this endpoint because giving premisson for one user to delete food is wrong maybe
# only the food created by him
