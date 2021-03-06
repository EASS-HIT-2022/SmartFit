from datetime import timedelta
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, status
from models.User import UserInDBBase
from fastapi.security import OAuth2PasswordRequestForm
from core.secuirty import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, Token
from ..deps import get_current_active_user
from fastapi.encoders import jsonable_encoder
router = APIRouter()


@router.post("/acsses_token", tags=["Login"], description='Provides an acsses token for one user, please login for FaspApi Authorize button', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> JSONResponse:
    user = await authenticate_user(
        form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    acsess_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    acsses_token = create_access_token(
        data={"sub": user.email}, expires_delta=acsess_token_expires
    )
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"access_token": acsses_token, "token_type": "bearer"})

## get user by token
@router.get("/me", tags=["Login"], description='Active User', response_model=UserInDBBase)
async def read_users_me(current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(current_user))
