from datetime import datetime


def test_get_rare(client, setup_teardown_db):
    response = client.get("/model/rare")

    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["doneness"] == "rare"
    assert response.json()["coefficients"] == {
        "thickness": 15,
        "bias": 10,
    }


def test_get_medium(client, setup_teardown_db):
    response = client.get("/model/medium")

    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["doneness"] == "medium"
    assert response.json()["coefficients"] == {
        "thickness": 1000,
        "bias": 100,
    }


def test_get_bad_doneness(client, setup_teardown_db):
    response = client.get("/model/not-implemented-yet")

    assert response.status_code == 404


def test_post(client, api_key, setup_teardown_db):
    response = client.post(
        "/model/",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "created": str(datetime(2023, 7, 31)),
            "doneness": "well",
            "coefficients": {
                "thickness": 999,
                "bias": 99,
            },
        },
    )

    assert response.status_code == 201
    assert response.json()["created"] == "2023-07-31T00:00:00"
    assert response.json()["doneness"] == "well"
    assert response.json()["coefficients"] == {
        "thickness": 999,
        "bias": 99,
    }
    assert "id" in response.json()


def test_post_unauthenticated(client, api_key, setup_teardown_db):
    response = client.post(
        "/model/",
        json={
            "created": str(datetime(2023, 7, 31)),
            "doneness": "well",
            "coefficients": {
                "thickness": 999,
                "bias": 99,
            },
        },
    )

    assert response.status_code == 401
