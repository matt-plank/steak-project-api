def test_get_rare(client, setup_teardown_db):
    response = client.get("/model/rare")

    assert response.status_code == 200
    assert response.json()["doneness"] == "rare"
    assert response.json()["coefficients"] == {
        "thickness": 15,
        "bias": 10,
    }


def test_get_medium(client, setup_teardown_db):
    response = client.get("/model/medium")

    assert response.status_code == 200
    assert response.json()["doneness"] == "medium"
    assert response.json()["coefficients"] == {
        "thickness": 1000,
        "bias": 100,
    }


def test_get_bad_doneness(client, setup_teardown_db):
    response = client.get("/model/not-implemented-yet")

    assert response.status_code == 404
