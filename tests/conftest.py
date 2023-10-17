import os

from fastapi.testclient import TestClient
from pytest import fixture

from steak_project_api.app import app


@fixture
def api_key():
    TEST_KEY: str = "my-test-key"

    os.environ["API_KEY"] = TEST_KEY
    yield TEST_KEY
    del os.environ["API_KEY"]


@fixture
def client():
    return TestClient(app)
