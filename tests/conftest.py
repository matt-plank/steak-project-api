from fastapi.testclient import TestClient
from pytest import fixture

TEST_KEY: str = "my-test-key"


@fixture
def app(monkeypatch):
    monkeypatch.setenv("API_KEY", TEST_KEY)

    from steak_project_api.app import app

    return app


@fixture
def client(app):
    return TestClient(app)


@fixture
def api_key():
    return TEST_KEY
