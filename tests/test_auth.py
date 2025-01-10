from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200

def test_login():
    response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
