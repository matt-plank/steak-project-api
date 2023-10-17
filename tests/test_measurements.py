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

    assert response.status_code == 200
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
