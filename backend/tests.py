import pytest
from fastapi.testclient import TestClient
import uuid
from main import app

client = TestClient(app)

@pytest.fixture
def client():
    return TestClient(app)