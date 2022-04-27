import asyncio

from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from app.backend.app.tests.utils.utils import create_random_user
from core.config import settings
from main import app
from .utils.utils import authentication_token_from_email


@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(app) as client:
        yield client
        
@pytest.fixture
async def normal_user_token_headers(client: TestClient):
    headers =  await authentication_token_from_email(
        client=client, email=settings.EMAIL_TEST_USER
    )
    return headers


@pytest.fixture
async def random_user():
    userindb = await create_random_user()
    return userindb
