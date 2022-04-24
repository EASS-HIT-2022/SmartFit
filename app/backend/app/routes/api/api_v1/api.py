from fastapi import APIRouter, Depends
from .endpoints import login, signup, profile, exrecise, food, workout, menu
from .endpoints.login import oauth_scheme

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(signup.router)
api_router.include_router(profile.router, dependencies=[
                          Depends(oauth_scheme)])
api_router.include_router(exrecise.router, dependencies=[
                          Depends(oauth_scheme)])
api_router.include_router(food.router, dependencies=[
                          Depends(oauth_scheme)])
api_router.include_router(workout.router, dependencies=[
                          Depends(oauth_scheme)])
api_router.include_router(menu.router, dependencies=[
                          Depends(oauth_scheme)])
