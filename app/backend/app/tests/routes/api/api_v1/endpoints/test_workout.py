from core.config import settings
from fastapi.testclient import TestClient
from db import db


USER_ID = '6d09a53a-94c2-4a13-b6cb-ab1f91bb29b7'
EXERCISE_ID = '000ssf-0s0s0v0-s0v0v0a0-0s0s0s1s0-0s0s0s0s0'

def test_create_user_workout(client: TestClient, normal_user_token_headers) -> None:
	response = client.post(
		f"{settings.API_V1_STR}/workout/new", headers=normal_user_token_headers, json=
				{
				"number_of_days_per_week": 3,
				"exercises": []
				}
		
	)
	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content


def test_get_my_workout(client: TestClient, normal_user_token_headers) -> None:
	response = client.get(
		f"{settings.API_V1_STR}/workout/", headers=normal_user_token_headers
	)

	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content


def test_edit_my_workout(client: TestClient, normal_user_token_headers) -> None:
	response = client.patch(
		f"{settings.API_V1_STR}/workout/", headers=normal_user_token_headers, json={
				'number_of_days_per_week': 4,
				'exercises': []
		}
	)
	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content
	assert content['number_of_days_per_week'] == 4


def test_get_user_workout(client: TestClient, normal_user_token_headers) -> None:
	response = client.get(
		f"{settings.API_V1_STR}/workout/{USER_ID}", headers=normal_user_token_headers
	)
	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert "_id" in content


def test_add_exercises(client: TestClient, normal_user_token_headers) -> None:
	response = client.post(
		f"{settings.API_V1_STR}/workout/add_exercises", headers=normal_user_token_headers,json={
			"id": "000ssf-0s0s0v0-s0v0v0a0-0s0s0s1s0-0s0s0s0s0",
			"name": "Bench Press",
			"alternatives": [],
			"favorite": False,
			"target_muscles": ["Pecs"],
			"Instructions": "lift the weights up and down",
			"Execution": "lift up and down",
		}
	)

	assert response.status_code == 200 or response.status_code == 201
	content = response.json()
	assert isinstance(content['exercises'], list) == True


def test_del_exercise(
    client: TestClient, normal_user_token_headers
) -> None:

	response = client.delete(
		f"{settings.API_V1_STR}/workout/delete_exercise?exercise_id={EXERCISE_ID}", headers=normal_user_token_headers,
	)

	assert response.status_code == 200 or response.status_code == 201

def test_del_exercise(
    client: TestClient, normal_user_token_headers
) -> None:

	response = client.delete(
		f"{settings.API_V1_STR}/workout/", headers=normal_user_token_headers,
	)

	assert response.status_code == 200 or response.status_code == 201

