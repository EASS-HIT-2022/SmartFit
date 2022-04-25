from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException, status
from models.User import UserInDBBase
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from db import db
router = APIRouter()


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
oauth_scheme = OAuth2PasswordBearer(tokenUrl='/api/api_v1/token')


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


async def get_current_user(token: str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if not token.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid token")
        token = token[7:]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = await get_user(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: UserInDBBase = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/api/api_v1/token", tags=["Login"], description='Provides an acsses token for one user, please login for FaspApi Authorize button', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> JSONResponse:
    user = await authenticate_user(
        form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"access_token": access_token, "token_type": "bearer"})


@router.get("/api/api_v1/users/me/", tags=["Login"], description='User Creation', response_model=UserInDBBase)
async def read_users_me(current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content=current_user)
