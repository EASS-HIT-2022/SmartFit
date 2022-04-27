import pytest
from core.config import settings
from models.User import UserCreate
from tests.utils.utils import random_email, random_lower_string
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from db import db



@pytest.mark.asyncio
async def test_create_user_existing_username(client:TestClient) -> None:
    email = random_email()
    password = random_lower_string()
    data = {"email": email, "password": password, "full_name": "test"}
    await db.get_collection("users").insert_one(jsonable_encoder(data))
    r = client.post(
        f"{settings.API_V1_STR}/signup/", json=data,
    )
    created_user = r.json()
    assert r.status_code == 404
    assert "_id" not in created_user



def test_create_user(client:TestClient):
    email = random_email()
    password = random_lower_string()
    user = UserCreate(email=email, password=password, full_name='test')
    response = client.post(
        f"{settings.API_V1_STR}/signup/", json=jsonable_encoder(user))
    assert response.status_code == 201
    assert '_id' in response.json()
