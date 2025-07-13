import pytest
from fastapi.testclient import TestClient
from app.main import app

def test_create_task(client: TestClient):
    """Тест создания задачи"""
    task_data = {
        "title": "Тестовая задача",
        "description": "Описание тестовой задачи",
        "is_completed": False
    }
    
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["description"] == task_data["description"]
    assert data["is_completed"] == task_data["is_completed"]
    assert "id" in data
    assert "created_at" in data

def test_get_tasks(client: TestClient):
    """Тест получения списка задач"""
    # Создаем несколько задач
    tasks = [
        {"title": "Задача 1", "description": "Описание 1"},
        {"title": "Задача 2", "description": "Описание 2"},
        {"title": "Задача 3", "description": "Описание 3"}
    ]
    
    for task in tasks:
        client.post("/tasks/", json=task)
    
    response = client.get("/tasks/")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) >= 3
    assert all("id" in task for task in data)
    assert all("title" in task for task in data)

def test_get_task(client: TestClient):
    """Тест получения одной задачи"""
    # Создаем задачу
    task_data = {"title": "Тестовая задача", "description": "Описание"}
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Получаем задачу
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == task_data["title"]

def test_get_task_not_found(client: TestClient):
    """Тест получения несуществующей задачи"""
    response = client.get("/tasks/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Задача не найдена"

def test_update_task(client: TestClient):
    """Тест обновления задачи"""
    # Создаем задачу
    task_data = {"title": "Исходная задача", "description": "Исходное описание"}
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Обновляем задачу
    update_data = {"title": "Обновленная задача", "is_completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["title"] == update_data["title"]
    assert data["is_completed"] == update_data["is_completed"]
    assert data["description"] == task_data["description"]  # Не изменилось

def test_update_task_not_found(client: TestClient):
    """Тест обновления несуществующей задачи"""
    update_data = {"title": "Обновленная задача"}
    response = client.put("/tasks/999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Задача не найдена"

def test_delete_task(client: TestClient):
    """Тест удаления задачи"""
    # Создаем задачу
    task_data = {"title": "Задача для удаления"}
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Удаляем задачу
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    
    # Проверяем, что задача удалена
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404

def test_delete_task_not_found(client: TestClient):
    """Тест удаления несуществующей задачи"""
    response = client.delete("/tasks/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Задача не найдена"

def test_task_validation(client: TestClient):
    """Тест валидации данных задачи"""
    # Пустой заголовок
    response = client.post("/tasks/", json={"title": "", "description": "Описание"})
    assert response.status_code == 422
    
    # Отсутствует заголовок
    response = client.post("/tasks/", json={"description": "Описание"})
    assert response.status_code == 422 