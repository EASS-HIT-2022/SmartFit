from datetime import datetime
from typing import List, Union
from fastapi import APIRouter, Body, Depends, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from matplotlib.font_manager import json_load
from sympy import Q
from models.User import UserInDBBase
from models.Food import Food
from models.Menu import Menu
from fastapi.responses import JSONResponse
from datetime import datetime
from db import db
from ..deps import get_current_active_user
import json



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


def multiple_appends(listname, *element):
    listname.extend(element)


@router.get("/", tags=["Menu"], description='Get my menu details')
async def my_menu(current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    if (menu := await db.get_collection("menu").find_one({"user_id": current_user.id})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=menu)
    raise HTTPException(
        status_code=404, detail=f"menu for current user not found")


@router.get("/{userid}", tags=["Menu"], description="Get user's menu details")
async def user_menu(userid: str) -> JSONResponse:
    if (menu := await db.get_collection("menu").find_one({"user_id": userid})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=menu)
    raise HTTPException(
        status_code=404, detail=f"menu for user {userid} not found")


@ router.delete("/", tags=["Menu"], description="Delete my menu")
async def my_menu_delete(current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    if (menu := await db.get_collection("menu").find_one({"user_id": current_user.id})) is not None:
        await db.get_collection("menu").delete_one({"user_id": current_user.id})
        return JSONResponse(
            status_code=201, content=f"menu for user {current_user.id} deleted")
    raise HTTPException(
        status_code=404, detail=f"menu for user {current_user.id} not found")


@ router.post("/add_food", tags=["Menu"], description="Add food to menu")
async def add_food_to_menu(current_user: UserInDBBase = Depends(get_current_active_user), food: Union[Food,List[Food]] = Body(...)) -> JSONResponse:
    try:
        menu = await my_menu(current_user)
    except HTTPException as e:
        raise HTTPException(
            status_code=404, detail=f"menu for current user not found")
    menu = json.loads(menu.body)
    menu = Menu(**menu)
    if menu.time_created == None:
        menu.time_created = datetime.now()
    if isinstance(food, Food):
        menu.foods.append(food)
    elif isinstance(food, List):
        menu.foods.extend(food)
    menu = jsonable_encoder(calc_menu_data(menu))
    result = await db.get_collection('menu').replace_one({'_id': menu['_id']}, menu)
    if result.modified_count == 1:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=menu)
    else:
        raise HTTPException(status_code=404, detail=f"Menu couldnt be updated")


@ router.delete("/delete_food", tags=["Menu"], description="Delete food from menu")
async def delete_food_from_menu(food_id: str,current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    try:
        menu = await my_menu(current_user)
    except HTTPException as e:
        raise HTTPException(
            status_code=404, detail=f"menu for current user not found")
    menu = json.loads(menu.body)
    menu = Menu(
        **{**menu, 'foods': [food for food in menu['foods'] if food['_id'] != food_id]})
    menu = jsonable_encoder(calc_menu_data(menu))
    result = await db.get_collection('menu').replace_one({'_id': menu['_id']}, menu)
    if result.modified_count == 1:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=menu)
    else:
        raise HTTPException(
            status_code=404, detail=f"Menu couldnt be updated")


@ router.post("/add_menu", tags=["Menu"], description="Add Menu")
async def add_menu(current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    if (menu := await db.get_collection("menu").find_one({"user_id": current_user.id})) is not None:
        raise HTTPException(
            status_code=404, detail=f"menu for user {current_user.id} already exists")
    menu_data = jsonable_encoder(
        Menu(user_id=current_user.id, foods=[], date=datetime.now()))
    new_menu_data = await db.get_collection("menu").insert_one(menu_data)
    created_menu = await db.get_collection("menu").find_one(
        {"_id": new_menu_data.inserted_id}
    )

    if created_menu is not None:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_menu)
    raise HTTPException(
        status_code=404, detail=f"Menu couldnt be created")
