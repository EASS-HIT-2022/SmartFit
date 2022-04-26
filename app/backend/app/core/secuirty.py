from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
from db import db
from models.User import UserInDBBase
from fastapi import Depends, HTTPException, status


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_user(email: str, db=db):
    user_dict = await db.get_collection("users").find_one({"email": email})
    if user_dict is not None:
        return UserInDBBase(**user_dict)
    else:
        raise HTTPException(status_code=401, detail="User not found")


async def authenticate_user(email: str, password: str, db=db):
    user = await get_user(email, db)
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect email or password")
    if not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=400, detail="Incorrect email or password")
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


