import os

from dotenv import load_dotenv
from fastapi.testclient import TestClient
from pymongo import MongoClient
from pytest import fixture

load_dotenv()


@fixture
def client(app):
    """The client used to make requests to the API."""
    return TestClient(app)


@fixture
def app(monkeypatch, patch_env_vars):
    """The FastAPI application for the client to request from.

    Fixtures to patch environment variables.
    Patch env vars before import to ensure access to api key and mongo credentials.
    """
    from steak_project_api.app import app

    return app


@fixture
def patch_env_vars(monkeypatch, api_key, test_db_name):
    """Patches required environment variables."""
    monkeypatch.setenv("API_KEY", api_key)
    monkeypatch.setenv("MONGO_DB", "steak_project")
    monkeypatch.setenv("MONGO_TEST_DB", test_db_name)


@fixture
def api_key():
    """The API key used to authenticate requests to the API."""
    return "my-test-key"


@fixture
def test_db_name():
    """The name of the test database."""
    return "steak_project_test"


@fixture
def setup_teardown_db(test_db_name):
    client = MongoClient(os.environ["MONGO_URI"])
    database = client[test_db_name]
    measurements = database.measurements

    measurements.insert_many(
        [
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
    )

    yield

    measurements.delete_many({})
