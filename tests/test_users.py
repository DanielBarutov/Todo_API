import pytest
from fastapi.testclient import TestClient
from app.main import app

def test_create_user(client: TestClient):
    """Тест создания пользователя"""
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword",
        "vacancy": "testvacancy"
    }
    
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]
    assert data["vacancy"] == user_data["vacancy"]
    assert "id" in data
    assert "created_at" in data

def test_get_users(client: TestClient):
    """Тест получения пользователей"""
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword",
        "vacancy": "testvacancy"
    }
    client.post("/users", json=user_data)
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["username"] == user_data["username"]
    assert data[0]["email"] == user_data["email"]
    assert data[0]["vacancy"] == user_data["vacancy"]
    