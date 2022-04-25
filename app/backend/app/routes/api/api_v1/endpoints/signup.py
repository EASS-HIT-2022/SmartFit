from fastapi import HTTPException, status
from datetime import datetime
from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from models.User import UserCreate, UserInDBBase
from fastapi.responses import JSONResponse
from .login import get_current_user, get_password_hash
from db import db
router = APIRouter()


@router.post("/api/api_v1/signup", tags=["Sign up"], description='User Creation')
async def signup(user: UserCreate = Body(...)) -> JSONResponse:
    if (userindb := await db.get_collection("users").find_one({"email": user.email})) is not None:
        raise HTTPException(
            status_code=404, detail=f"User {user.email} already exist")

    userindb = UserInDBBase(
        **user.dict(), create_date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        password_hash=get_password_hash(password=user.password))

    await db.get_collection("users").insert_one(jsonable_encoder(userindb))

    created_user = await db.get_collection("users").find_one(
        {"email": user.email}
    )

    if created_user is not None:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={**created_user, 'password_hash': created_user['password_hash']})
    raise HTTPException(
        status_code=400, detail=f"User {user.email} couldnt be created")
