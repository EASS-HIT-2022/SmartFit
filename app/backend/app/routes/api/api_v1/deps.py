
from fastapi import Depends, HTTPException, status
from core.secuirty import TokenData, SECRET_KEY, ALGORITHM, get_user
from core.config import settings
from models.User import UserInDBBase
from fastapi import HTTPException, status
from jose import jwt
from jose.exceptions import JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends, HTTPException, status

oauth_scheme = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/login/acsses_token')


async def get_current_user(token: str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
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
