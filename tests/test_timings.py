def test_post(client):
    response = client.post(
        "/timing/",
        json={"thickness": 2.5},
    )

    assert response.status_code == 200
    assert response.json() == {
        "rare": 75.0,
        "midRare": 100.0,
        "medium": 125.0,
        "midWell": 150.0,
        "well": 175.0,
    }


def test_post_no_thickness(client):
    response = client.post(
        "/timing/",
        json={"bad": "data"},
    )

    assert response.status_code == 400
    assert response.json() == {
        "message": "You must provide a thickness",
    }
