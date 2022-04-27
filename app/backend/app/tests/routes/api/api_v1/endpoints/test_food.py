import pytest
from core.config import settings
from fastapi.testclient import TestClient
from db import db
from .....utils.utils import create_random_item_without_owner, random_lower_string,random_number



@pytest.mark.asyncio
async def test_get_food_by_id(client: TestClient, normal_user_token_headers) -> None:
	item_in = await create_random_item_without_owner('food')
	item_in_id = str(item_in.inserted_id)

	response = client.get(
		f"{settings.API_V1_STR}/nutrition/{item_in_id}", headers=normal_user_token_headers
	)

	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content




def test_get_all_food(
    client: TestClient,normal_user_token_headers
) -> None:

    response = client.get(
        f"{settings.API_V1_STR}/nutrition/", headers=normal_user_token_headers
    )

    assert response.status_code == 200 or response.status_code == 201


def test_post_food(client: TestClient, normal_user_token_headers) -> None:
	response = client.post(
		f"{settings.API_V1_STR}/nutrition/new", headers=normal_user_token_headers,json={
			    'name': random_lower_string(),
				'grams': random_number(),
				'type': random_lower_string(),
				'calories': random_number(),
				'fat': random_number(),
				'carbs': random_number(),
				'protein': random_number(),
		}
	)

	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content