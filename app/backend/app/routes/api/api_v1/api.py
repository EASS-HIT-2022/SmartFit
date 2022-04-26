from fastapi import APIRouter, Depends
from .endpoints import login, signup, profile, exrecise, food, workout, menu
from .deps import oauth_scheme

api_router = APIRouter()
api_router.include_router(login.router, prefix='/login')
api_router.include_router(signup.router, prefix='/signup')
api_router.include_router(profile.router, dependencies=[
                          Depends(oauth_scheme)], prefix='/profile')
api_router.include_router(exrecise.router, dependencies=[
                          Depends(oauth_scheme)], prefix='/exrecise')
api_router.include_router(food.router, dependencies=[
                          Depends(oauth_scheme)], prefix='/nutrition')
api_router.include_router(workout.router, dependencies=[
                          Depends(oauth_scheme)], prefix='/workout')
api_router.include_router(menu.router, dependencies=[
                          Depends(oauth_scheme)], prefix='/menu')
