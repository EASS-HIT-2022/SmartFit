from fastapi import APIRouter, Body, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse

from ..deps import get_current_active_user
from models.Profile import Profile, ProfileCreate,ProfileUpdate
from models.User import UserInDBBase
from fastapi.encoders import jsonable_encoder
from db import db
import json
router = APIRouter()


@router.get("/", tags=['Profile'], response_model=Profile, description='Get my profile details')
async def my_profile(current_user: UserInDBBase = Depends(get_current_active_user)) -> JSONResponse:
    if (profile := await db.get_collection("profile").find_one({"user_id": current_user.id})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=profile)
    raise HTTPException(
        status_code=404, detail=f"profile for current user not found")


@ router.post("/new", tags=["Profile"], description='Add a new profile')
async def my_profile_create(current_user: UserInDBBase = Depends(get_current_active_user), profile: ProfileCreate = Body(...)) -> JSONResponse:
    if (profile_ := await db.get_collection("profile").find_one({"user_id": current_user.id})) is not None:
        raise HTTPException(
            status_code=404, detail=f"profile for user {current_user.id} already exists")
    user_profile = jsonable_encoder(Profile(**profile.dict(), user_id=current_user.id))
    profile_insert_res = await db.get_collection("profile").insert_one(user_profile)
    created_profile = await db.get_collection("profile").find_one(
        {"_id": profile_insert_res.inserted_id}
    )
    if created_profile is not None:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_profile)
    raise HTTPException(
        status_code=404, detail=f"Profile couldnt be created")


@ router.patch("/edit", tags=["Profile"], description='Edit my profile')
async def my_profile_edit(current_user: UserInDBBase = Depends(get_current_active_user), profile: ProfileUpdate = Body(..., example={
    'weight': 75,
    'height':190,
    'age': 25,
    'BMI': 110,
    'is_premium': False,
    'premium_until': None,
    'fav_split': 'AB',
    'goal': 'Gain Weight'
})):
    my_profil = await my_profile(current_user)
    my_profil = json.loads(my_profil.body)
    my_stored_profile = Profile(**my_profil)
    update_data = profile.dict(exclude_unset=True)
    updated_profile = my_stored_profile.copy(update=update_data)
    updated_profile = jsonable_encoder(updated_profile)

    result = await db.get_collection("profile").update_one({'_id': updated_profile['_id']}, {'$set': updated_profile})
    if result.modified_count == 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content='Profile not updated')
    profile_updated = await db.get_collection("profile").find_one({'_id': updated_profile['_id']})
    return JSONResponse(status_code=status.HTTP_200_OK, content=profile_updated)


@ router.get("/{userid}", tags=["Profile"], description='Get other user profile')
async def other_profile(userid: str):
    if (profile := await db.get_collection("profile").find_one({"user_id": userid})) is not None:
        return profile
    raise HTTPException(
        status_code=404, detail=f"profile for user {userid} not found")


@ router.get("/profiles/all", tags=["Profile"], description='Get all profiles')
async def all_profiles():
    if (profiles := db.get_collection("profile").find()) is not None:
        return await profiles.to_list(200)

    raise HTTPException(
        status_code=404, detail=f"no profiles found")


@ router.delete("/del", tags=["Profile"], description='Delete my profile')
async def del_my_profile(current_user: UserInDBBase = Depends(get_current_active_user)):
    my_profile_ = await my_profile(current_user)
    my_profile_ = json.loads(my_profile_.body)
    if (profile := await db.get_collection("profile").find_one_and_delete({"_id": my_profile_['_id']})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=profile)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='No profile found')
