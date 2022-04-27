import random
import pytest
import string 
from db import db
from typing import Dict
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from core.config import settings
from models.User import UserCreate
from db import db
import pytest
from core.secuirty import get_password_hash

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"

def random_number() -> int:
    return random.randint(1, 100)

def random_number_interval(a,b) ->int:
    return random.randint(a,b)

@pytest.mark.asyncio
async def create_random_item_with_owner(collection_name,owner_id = None):
    if owner_id is None:
        user = await create_random_user()
        owner_id = user
    name = random_lower_string()
    _id = random_lower_string()
    item_in = {'name':name,'user_id':owner_id,'_id':_id}
    
    try:
        item_in = await db.get_collection(collection_name).insert_one(item_in)
    except Exception as e:
        raise e

    return _id
    
@pytest.mark.asyncio    
async def create_random_item_without_owner(collection_name):
    name = random_lower_string()
    _id = random_lower_string()
    item_in = {'name':name,'_id':_id}
    
    try:
        item_in_db = await db.get_collection(collection_name).insert_one(item_in)
    except Exception as e:
        raise e
    
    return item_in_db


def user_authentication_headers(
    client: TestClient, email: str, password: str
) -> Dict[str, str]:
    form = {'username' : email, 'password' : password}

    r = client.post(f"{settings.API_V1_STR}/login/acsses_token", data=form)

    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


@pytest.mark.asyncio
async def create_random_user():
    email = random_email()
    password = random_lower_string()
    full_name = random_lower_string()
    _id = random_lower_string()
    password_hash = get_password_hash(password)
    user_in = {'email':email,'password':password,'full_name':full_name,'_id':_id,'password_hash':password_hash}
    try:
        userindb = await db.get_collection('users').insert_one(user_in)
    except Exception as e:
        raise 'error user was not created'
    return user_in


@pytest.mark.asyncio
async def authentication_token_from_email(
         client: TestClient, email: str) -> Dict[str, str]:
    """
    Return a valid token for the user with given email.
    If the user doesn't exist it is created first.
    """
    password = f'{settings.PASSWORD_TEST_USER}'
    user = await db.get_collection('users').find_one({'email': email})

    if not user:
        user_in_create = UserCreate(
            email=email, full_name=email, password=password)
        user = db.get_collection('users').insert_one(
            jsonable_encoder(user_in_create))
        
    return user_authentication_headers(client=client, email=email, password=password)
