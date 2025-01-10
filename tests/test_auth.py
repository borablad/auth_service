from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200

def test_login():
    response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200

def test_user_access_denied():
    user_token = login_as_user()  # Получить токен обычного пользователя
    response = client.get("/users", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code == 403

def test_admin_access():
    admin_token = login_as_admin()  # Получить токен администратора
    response = client.get("/users", headers={"Authorization": f"Bearer {admin_token}"})
    assert response.status_code == 200