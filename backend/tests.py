import pytest
from fastapi.testclient import TestClient
import uuid
from main import app

client = TestClient(app)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def creatingAStudent(client):
    feedback = client.post("/students/", params = {"name": "T1", "wallet" : 100.00})
    assert feedback.status_code == 200
    return feedback.json()

def testCreatingAStudent(client):
    feedback = client.post("/students/", params = {"name": "Barry Allen", "wallet" : 100.00})
    student_created = feedback.json()

    assert feedback.status_code == 200
    assert student_created['name'] == "Barry Allen"
    assert student_created['wallet'] == 100.00
    assert 'id' in student_created

@pytest.fixture
def creatingAGroupOrder(client):
    pass