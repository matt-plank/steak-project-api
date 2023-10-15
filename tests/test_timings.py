from fastapi.testclient import TestClient

from app.app import app


def test_create():
    client = TestClient(app)

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
