from fastapi import HTTPException, status
from datetime import datetime
from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from models.User import UserCreate, UserInDBBase
from fastapi.responses import JSONResponse
from core.secuirty import get_password_hash
from db import db
router = APIRouter()


@router.post("/", tags=["Sign up"], description='User Creation')
async def signup(user: UserCreate = Body(...)) -> JSONResponse:
    if (userindb := await db.get_collection("users").find_one({"email": user.email})) is not None:
        raise HTTPException(
            status_code=404, detail=f"User {user.email} already exist")
    print(user)
    userindb = UserInDBBase(
        full_name=user.full_name,email=user.email.lower(), create_date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        password_hash=get_password_hash(user.password))

    await db.get_collection("users").insert_one(jsonable_encoder(userindb))

    created_user = await db.get_collection("users").find_one(
        {"email": user.email}
    )

    if created_user is not None:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={**created_user, 'password_hash': created_user['password_hash']})
    raise HTTPException(
        status_code=400, detail=f"User {user.email} couldnt be created")
