def test_get(client, setup_teardown_db):
    response = client.get("/measurement/")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_post(client, api_key, setup_teardown_db):
    response = client.post(
        "/measurement/",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "MEDIUM",
        },
    )

    assert response.status_code == 201
    assert "thickness" in response.json()
    assert "cookTime" in response.json()
    assert "doneness" in response.json()
    assert "id" in response.json()


def test_post_no_auth(client, setup_teardown_db):
    response = client.post(
        "/measurement/",
        json={
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "MEDIUM",
        },
    )

    assert response.status_code == 401


def test_post_invalid_auth(client, setup_teardown_db):
    response = client.post(
        "/measurement/",
        headers={
            "Authorization": "asdasdasdasd",
        },
        json={
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "MEDIUM",
        },
    )

    assert response.status_code == 401


def test_post_incorrect_auth(client, setup_teardown_db):
    response = client.post(
        "/measurement/",
        headers={
            "Authorization": "Bearer bad-api-key",
        },
        json={
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "MEDIUM",
        },
    )

    assert response.status_code == 401


def test_post_no_thickness(client, api_key):
    response = client.post(
        "/measurement/",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "cookTime": 90,
            "doneness": "MEDIUM",
        },
    )

    assert response.status_code == 422


def test_post_no_cookTime(client, api_key):
    response = client.post(
        "/measurement/",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "thickness": 2.5,
            "doneness": "MEDIUM",
        },
    )

    assert response.status_code == 422


def test_post_no_doneness(client, api_key):
    response = client.post(
        "/measurement/",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "thickness": 2.5,
            "cookTime": 90,
        },
    )

    assert response.status_code == 422


def test_post_bad_doneness(client, api_key):
    response = client.post(
        "/measurement/",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "MEDIUM_WELL",
        },
    )

    assert response.status_code == 422
