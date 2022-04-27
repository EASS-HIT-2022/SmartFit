import pytest
from core.config import settings
from fastapi.testclient import TestClient
from .....utils.utils import create_random_item_with_owner,create_random_item_without_owner


@pytest.mark.asyncio
async def test_get_ex_by_id(client: TestClient, normal_user_token_headers) -> None:
    item_in = await create_random_item_without_owner('exercises')
    item_in_id = str(item_in.inserted_id)
    response = client.get(
        f"{settings.API_V1_STR}/exrecise/{item_in_id}", headers=normal_user_token_headers
    )

    assert response.status_code == 200 or response.status_code == 201
    content = response.json()
    assert "_id" in content



def test_get_all_ex(
    client: TestClient,normal_user_token_headers
) -> None:

    response = client.get(
        f"{settings.API_V1_STR}/exrecise/", headers=normal_user_token_headers
    )
    assert response.status_code == 200 or response.status_code == 201

