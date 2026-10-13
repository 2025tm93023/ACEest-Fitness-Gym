from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "Application is running"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "UP"


def test_get_members():
    client = app.test_client()

    response = client.get("/members")

    assert response.status_code == 200
    assert len(response.json) >= 2


def test_get_existing_member():
    client = app.test_client()

    response = client.get("/members/1")

    assert response.status_code == 200
    assert response.json["name"] == "Rahul"


def test_get_non_existing_member():
    client = app.test_client()

    response = client.get("/members/999")

    assert response.status_code == 404


def test_add_member():
    client = app.test_client()

    response = client.post(
        "/members",
        json={
            "name": "Amit",
            "age": 30,
            "membership": "Premium"
        }
    )

    assert response.status_code == 201
    assert response.json["name"] == "Amit"