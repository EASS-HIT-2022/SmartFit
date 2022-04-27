from core.config import settings
from fastapi.testclient import TestClient
from .....utils.utils import  random_number_interval

USER_ID = '6d09a53a-94c2-4a13-b6cb-ab1f91bb29b7'

def test_create_user_profile(client: TestClient, normal_user_token_headers) -> None:
	response = client.post(
		f"{settings.API_V1_STR}/profile/new", headers=normal_user_token_headers ,json={
				'email': settings.EMAIL_TEST_USER,
				'height': random_number_interval(100,300),
				'weight': random_number_interval(40,200),
				'age': random_number_interval(12,120)
		}
	)
	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content


def test_get_my_profile(client: TestClient, normal_user_token_headers) -> None:
	response = client.get(
		f"{settings.API_V1_STR}/profile/", headers=normal_user_token_headers
	)

	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content


def test_edit_my_pofile(client: TestClient, normal_user_token_headers) -> None:
	response = client.patch(
		f"{settings.API_V1_STR}/profile/edit", headers=normal_user_token_headers,json={
				"email":'exaxa@exa.com',
				'height':190,
				"weight": 75,
				"age": 25,
				"BMI": 110,
				"is_premium": False,
				"fav_split": "AB",
				"goal": "Gain Weight"
		}	
	)
	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content
	assert content['age'] == 25


def test_get_user_profile(client: TestClient, normal_user_token_headers) -> None:
	response = client.get(
		f"{settings.API_V1_STR}/profile/{USER_ID}", headers=normal_user_token_headers
	)
	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content


def test_get_all_profiles(client: TestClient, normal_user_token_headers) -> None:
	response = client.get(
		f"{settings.API_V1_STR}/profile/profiles/all", headers=normal_user_token_headers
	)

	assert response.status_code == 200 or response.status_code == 201
	content = response.json()

	assert isinstance(content,list) ==True


def test_del_my_profile(
    client: TestClient, normal_user_token_headers
) -> None:

	response = client.delete(
		f"{settings.API_V1_STR}/profile/del", headers=normal_user_token_headers
	)
 
	assert response.status_code == 200 or response.status_code == 201
