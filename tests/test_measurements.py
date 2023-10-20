def test_get(client):
    response = client.get("/measurement/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "RARE",
        },
        {
            "thickness": 2.5,
            "cookTime": 120,
            "doneness": "MEDIUM",
        },
    ]


def test_post(client, api_key):
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
    assert response.json() == {
        "thickness": 2.5,
        "cookTime": 90,
        "doneness": "MEDIUM",
    }


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

    assert response.status_code == 400
    assert response.json() == {
        "message": "thickness is required",
    }


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

    assert response.status_code == 400
    assert response.json() == {
        "message": "cookTime is required",
    }


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

    assert response.status_code == 400
    assert response.json() == {
        "message": "doneness is required",
    }


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

    assert response.status_code == 400
    assert response.json() == {
        "message": "MEDIUM_WELL is not a valid Doneness",
    }


def test_post_no_authorization_header(client):
    response = client.post(
        "/measurement/",
        json={
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "MEDIUM",
        },
    )

    assert response.status_code == 401
    assert response.json() == {"message": "Authorization required"}


def test_post_invalid_authorization_header(client, api_key):
    response = client.post(
        "/measurement/",
        headers={
            "Authorization": api_key,
        },
        json={
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "MEDIUM",
        },
    )

    assert response.status_code == 401
    assert response.json() == {"message": "Improperly formatted Authorization header"}


def test_post_invalid_key(client):
    response = client.post(
        "/measurement/",
        headers={
            "Authorization": "Bearer invalid-token-hehehe",
        },
        json={
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "MEDIUM",
        },
    )

    assert response.status_code == 401
    assert response.json() == {"message": "Invalid API key"}
