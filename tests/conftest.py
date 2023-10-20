from unittest import mock

from fastapi.testclient import TestClient
from pytest import fixture

from .mocks.client import client_mock

TEST_KEY: str = "my-test-key"


@fixture
def client(app):
    return TestClient(app)


@fixture
def app(monkeypatch, patch_env_vars, patch_mongo):
    from steak_project_api.app import app

    return app


@fixture
def patch_env_vars(monkeypatch, api_key):
    monkeypatch.setenv("MONGO_USERNAME", "my-test-username")
    monkeypatch.setenv("MONGO_PASSWORD", "my-test-password")
    monkeypatch.setenv("API_KEY", api_key)


@fixture
def api_key():
    return TEST_KEY


@fixture
def patch_mongo(monkeypatch, mongo_client_mock):
    monkeypatch.setattr(
        "pymongo.MongoClient",
        mongo_client_mock,
    )


@fixture
def mongo_client_mock():
    return client_mock
