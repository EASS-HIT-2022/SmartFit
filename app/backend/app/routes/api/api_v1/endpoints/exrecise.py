from typing import List
from fastapi import APIRouter, HTTPException, status
from models.Exercise import Exercise
from db import db
from fastapi.responses import JSONResponse
import requests
router = APIRouter()

headers = {
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com",
	"X-RapidAPI-Key": "64e2f185e8msh834237bd8e7387dp16b82fjsncaefad30e0e6"
}

base_url = "https://exercisedb.p.rapidapi.com/exercises"


@router.get("/target_muscles", tags=["Exercise"], description='Get all target muscles details')
def get_list_of_target_muscles() -> JSONResponse:
    try:
        target_muscles = requests.request('GET',base_url+'/targetList',headers=headers)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=target_muscles.json())
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Target Muscles not Found")



@router.get("/name/{name}", tags=["Exercise"], description='Get speseific exrecise details')
async def get_exrecise_by_name(name: str) -> JSONResponse:
    try:
        exrecise = requests.request('GET',base_url+'/name/'+name,headers=headers)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=exrecise.json())
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Exrecise not Found")

@router.get("/{id}", tags=["Exercise"], description='Get speseific exrecise details')
async def get_exrecise_by_id(id: str) -> JSONResponse:
    try:
        exrecise = requests.request('GET',base_url+'/exercise/'+id,headers=headers)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=exrecise.json())
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Exrecise not Found")


@router.get("/target_muscles/{muscle}", tags=["Exercise"], description='Get all exrecises for a spesific target muscle')
def get_list_of_exrecises_of_target_muscle(muscle:str) -> JSONResponse:
    try:
        target_muscles = requests.request('GET',base_url+'/target/'+muscle,headers=headers)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=target_muscles.json())
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Target Muscles not Found")



@router.get("/", tags=["Exercise"], description='Get all exrecises')
def get_list_of_all_exrecises() -> JSONResponse:
    try:
        exrecises = requests.request('GET',base_url,headers=headers)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=exrecises.json())
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Target Muscles not Found")