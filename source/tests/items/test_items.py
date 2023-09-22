from api.items import schemas
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# /items test cases
def test_get_valid_endpoint():
    # default: offset = 0 limit = 25
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list) is True
    assert len(response.json()) == 25

    limit: int = 30
    offset: int = 30
    response = client.get(f"/items?offset={offset}&limit={limit}")
    assert response.status_code == 200
    assert isinstance(response.json(), list) is True
    assert response.json()[0].get("id") == offset + 1  # if had no deletions from db in past
    assert len(response.json()) == limit

    valid_id: int = 1
    response = client.get(f"/items/{valid_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict) is True
    assert response.json().get("id") == valid_id


def test_get_invalid_endpoint():
    # mistake
    response = client.get("/itemss")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
    # valid but too large and not existing yet
    response = client.get("/items/1000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Requested object does not exists..."}
    # invalid
    response = client.get("/items/a")
    assert response.status_code == 422
    assert response.json() == {
        'detail':
            [
                {
                    'type': 'int_parsing', 'loc': ['path', 'item_id'],
                    'msg': 'Input should be a valid integer, unable to parse string as an integer',
                    'input': 'a', 'url': 'https://errors.pydantic.dev/2.3/v/int_parsing'
                }
            ],
        'body': None
    }


def test_post_valid_body():
    body: dict = {"name": "Random Item Test"}
    response = client.post("/tests/items/", json=body)
    assert response.status_code == 200
    assert body.get("name") in response.json().get("name")
    assert response.json().get("id") is not None


def test_post_invalid_body():
    # Invalid type
    value: int = 1
    body = {"name": value}
    response = client.post("/tests/items/", json=body)
    assert response.status_code == 422
    assert response.json() == {
                                    "detail": [
                                        {
                                            "type": "string_type", "loc": ["body", "name"],
                                            "msg": "Input should be a valid string", "input": value,
                                            "url": "https://errors.pydantic.dev/2.3/v/string_type"
                                        }
                                    ],
                                    "body": {
                                        "name": value
                                    }
    }


