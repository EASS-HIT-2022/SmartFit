from core.config import settings
from fastapi.testclient import TestClient
from .....utils.utils import random_lower_string,random_number

FOOD_ID ='5e9f8f8f8f8f8f8f8f8f8f8'

# if test menu has a menu tests will fail need to delete them from db before running tests

def test_create_user_base_menu(client: TestClient, normal_user_token_headers) -> None:
	response = client.post(
		f"{settings.API_V1_STR}/menu/add_menu", headers=normal_user_token_headers
	)

	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content


def test_get_menu(client: TestClient, normal_user_token_headers) -> None:
	response = client.get(
		f"{settings.API_V1_STR}/menu/", headers=normal_user_token_headers
	)

	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content




def test_get_user_menu(client: TestClient, normal_user_token_headers) -> None:
	userid = settings.TEST_USER_ID
	response = client.get(
		f"{settings.API_V1_STR}/menu/{userid}", headers=normal_user_token_headers
	)
	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content



def test_add_my_menu_food(client: TestClient, normal_user_token_headers) -> None:
	response = client.post(
		f"{settings.API_V1_STR}/menu/add_food", headers=normal_user_token_headers,json={
				'_id':FOOD_ID,
			    'name': random_lower_string(),
				'grams': random_number(),
				'type': random_lower_string(),
				'calories': random_number(),
				'fat': random_number(),
				'carbs': random_number(),
				'protein': random_number(),
				'alternatives': [],

		}
	)
	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content


def test_del_food_from_my_menu(client: TestClient, normal_user_token_headers) -> None:
	response = client.delete(
		f"{settings.API_V1_STR}/menu/delete_food?food_id={FOOD_ID}", headers=normal_user_token_headers
	)
	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content




def test_del_my_menu(
    client: TestClient, normal_user_token_headers
) -> None:

    response = client.delete(
        f"{settings.API_V1_STR}/menu/", headers=normal_user_token_headers
    )

    assert response.status_code == 200 or response.status_code == 201



# user_authentication_headers(client,email = random_user['email'],password = random_user['password'])


