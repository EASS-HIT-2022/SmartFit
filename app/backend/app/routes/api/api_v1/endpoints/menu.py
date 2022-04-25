from datetime import datetime
from typing import List
from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from models.Food import Food
from models.Menu import Menu, MenuBase
from fastapi.responses import JSONResponse
from datetime import datetime
from db import db
from .login import get_current_user

router = APIRouter()


def calc_menu_data(menu: Menu):
    total_calories = 0
    calories_from_fat = 0
    calories_from_protien = 0
    calories_from_carbs = 0
    for food in menu.foods:
        total_calories += food.calories
        calories_from_fat += food.fat
        calories_from_protien += food.protein
        calories_from_carbs += food.carbs
    menu.total_calories, menu.calories_from_fat, menu.calories_from_protien, menu.calories_from_carbs = total_calories, calories_from_fat, calories_from_protien, calories_from_carbs
    return menu


@router.get("/api/api_v1/nutrition/menu", tags=["Menu"], description='Get my menu details')
async def my_menu(request: Request) -> JSONResponse:
    user = await get_current_user(request.headers['Authorization'])
    if (menu := await db.get_collection("menu").find_one({"user_id": user.id})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=menu)
    raise HTTPException(
        status_code=404, detail=f"menu for current user not found")


@router.get("/api/api_v1/{userid}/menu", tags=["Menu"], description="Get user's menu details")
async def user_menu(userid: str) -> JSONResponse:
    if (menu := await db.get_collection("menu").find_one({"user_id": userid})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=menu)
    raise HTTPException(
        status_code=404, detail=f"menu for user {userid} not found")


@ router.delete("/api/api_v1/nutrition/menu", tags=["Menu"], description="Delete my menu")
async def my_menu_delete(request: Request) -> JSONResponse:
    user = await get_current_user(request.headers['Authorization'])
    if (menu := await db.get_collection("menu").find_one({"user_id": user.id})) is not None:
        await db.get_collection("menu").delete_one({"user_id": user.id})
        return JSONResponse(
            status_code=201, content=f"menu for user {user.id} deleted")
    raise HTTPException(
        status_code=404, detail=f"menu for user {user.id} not found")


@ router.post("/api/api_v1/nutrition/menu/add_food", tags=["Menu"], description="Add food to menu")
async def add_food_to_menu(request: Request, food: List[Food] = Body(...)) -> JSONResponse:
    try:
        menu = await my_menu(request)
    except HTTPException as e:
        raise HTTPException(
            status_code=404, detail=f"menu for current user not found")
    menu = Menu(**menu)
    if menu.time_created == None:
        menu.time_created = datetime.now()
    menu.foods.extend(food)
    menu = jsonable_encoder(calc_menu_data(menu))
    result = await db.get_collection('menu').replace_one({'_id': menu['_id']}, menu)
    if result.modified_count == 1:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=menu)
    else:
        raise HTTPException(status_code=404, detail=f"Menu couldnt be updated")


@ router.delete("/api/api_v1/nutrition/menu/delete_food", tags=["Menu"], description="Delete food from menu")
async def delete_food_from_menu(request: Request, food_id: str) -> JSONResponse:
    try:
        menu = await my_menu(request)
    except HTTPException as e:
        raise HTTPException(
            status_code=404, detail=f"menu for current user not found")

    menu = Menu(
        **{**menu, 'foods': [food for food in menu['foods'] if food['_id'] != food_id]})
    menu = jsonable_encoder(calc_menu_data(menu))
    result = await db.get_collection('menu').replace_one({'_id': menu['_id']}, menu)
    if result.modified_count == 1:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=menu)
    else:
        raise HTTPException(
            status_code=404, detail=f"Menu couldnt be updated")


@ router.post("/api/api_v1/nutrition/menu/add_menu", tags=["Menu"], description="Add Menu")
async def add_menu(request: Request) -> JSONResponse:
    user = await get_current_user(request.headers['Authorization'])
    if (menu := await db.get_collection("menu").find_one({"user_id": user.id})) is not None:
        raise HTTPException(
            status_code=404, detail=f"menu for user {user.id} already exists")
    menu_data = jsonable_encoder(
        Menu(user_id=user.id, foods=[], date=datetime.now()))
    new_menu_data = await db.get_collection("menu").insert_one(menu_data)
    created_menu = await db.get_collection("menu").find_one(
        {"_id": new_menu_data.inserted_id}
    )

    if created_menu is not None:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_menu)
    raise HTTPException(
        status_code=404, detail=f"Menu couldnt be created")
