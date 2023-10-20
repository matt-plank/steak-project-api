from fastapi.testclient import TestClient
from pytest import fixture

from .mocks.client import client_mock


@fixture
def client(app):
    """The client used to make requests to the API."""
    return TestClient(app)


@fixture
def app(monkeypatch, patch_env_vars, patch_mongo):
    """The FastAPI application for the client to request from.

    Fixtures to patch environment variables and MongoDB client.
    Patch env vars before import to ensure access to api key and mongo credentials.
    """
    from steak_project_api.app import app

    return app


@fixture
def patch_env_vars(monkeypatch, api_key):
    """Patches required environment variables."""
    monkeypatch.setenv("MONGO_USERNAME", "my-test-username")
    monkeypatch.setenv("MONGO_PASSWORD", "my-test-password")
    monkeypatch.setenv("API_KEY", api_key)


@fixture
def api_key():
    """The API key used to authenticate requests to the API."""
    return "my-test-key"


@fixture
def patch_mongo(monkeypatch, mongo_client_mock):
    """Patches the MongoDB client with a fake data source."""
    monkeypatch.setattr(
        "pymongo.MongoClient",
        mongo_client_mock,
    )


@fixture
def mongo_client_mock():
    """Fake MongoDB client used to prevent the need for deployed database."""
    return client_mock
