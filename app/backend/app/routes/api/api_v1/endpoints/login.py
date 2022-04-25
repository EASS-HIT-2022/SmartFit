from datetime import timedelta
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, status
from models.User import UserInDBBase
from fastapi.security import OAuth2PasswordRequestForm
from core.secuirty import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, Token
from ..deps import get_current_active_user
router = APIRouter()


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
