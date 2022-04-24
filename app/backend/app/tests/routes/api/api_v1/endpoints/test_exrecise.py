from fastapi.testclient import TestClient
from ......main import app


client = TestClient(app)


def test_get_exercise():
    pass


def test_get_all_exrecise():
    response = client.get("/api/api_v1/exercises")
    assert response.status_code == 200
    assert response.json() == [
        {
            "_id": "5e9f9f9f9f9f9f9f9f9f9f9",
            "name": "Bench Press",
                    "description": "Bench Press",
                    "image": 'str'
        }]
