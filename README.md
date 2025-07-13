# ToDo API

Полнофункциональное REST API для управления задачами, построенное на FastAPI с использованием современных практик разработки.

## 🚀 Возможности

- ✅ CRUD операции для задач
- 🗄️ SQLAlchemy ORM с поддержкой миграций
- 📚 Автоматическая документация API (Swagger/ReDoc)
- 🗄️ SQLAlchemy ORM с поддержкой миграций

## 🛠️ Технологический стек

- **FastAPI** - современный веб-фреймворк для Python
- **SQLAlchemy** - ORM для работы с базой данных
- **Alembic** - система миграций
- **Pydantic** - валидация данных
- **Pytest** - тестирование
- **SQLite** - база данных (можно заменить на PostgreSQL)

## 🛠️ Технологический стек

### Предварительные требования

- Python 3.9+
- pip

### Локальная установка

1. **Клонируйте репозиторий:**
```bash
git clone <repository-url>
cd todo-api
```

2. **Создайте виртуальное окружение:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

4. **Настройте переменные окружения:**
```bash
cp .env.example .env
# Отредактируйте .env файл при необходимости
```

5. **Запустите миграции:**
```bash
alembic upgrade head
```

6. **Запустите сервер:**
```bash
uvicorn app.main:app --reload
```

API будет доступно по адресу: http://localhost:8000

## 📚 Автоматическая документация API (Swagger/ReDoc)

После запуска сервера документация доступна по следующим адресам:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Тестирование

### Запуск тестов
```bash
pytest tests/ -v
```

### Запуск тестов с покрытием
```bash
pytest tests/ -v --cov=app --cov-report=html
```

## 📋 Примеры использования

### Создание задачи
```bash
curl -X POST "http://localhost:8000/tasks/" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Изучить FastAPI",
       "description": "Изучить документацию и создать первый проект",
       "is_completed": false
     }'
```

### Получение списка задач
```bash
curl -X GET "http://localhost:8000/tasks/"
```

### Получение конкретной задачи
```bash
curl -X GET "http://localhost:8000/tasks/1"
```

### Обновление задачи
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Изучить FastAPI (обновлено)",
       "is_completed": true
     }'
```

### Удаление задачи
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

## 📋 Примеры использования

## 📋 Примеры использования

```
todo-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # Точка входа приложения
│   ├── models.py        # SQLAlchemy модели
│   ├── schemas.py       # Pydantic схемы
│   ├── crud.py          # CRUD операции
│   ├── routes.py        # API endpoints
│   └── database.py      # Конфигурация БД
├── alembic/             # Миграции базы данных
├── tests/               # Тесты
│   ├── __init__.py
│   ├── conftest.py      # Конфигурация pytest
│   └── test_tasks.py    # Тесты для задач
├── .github/workflows/   # CI/CD
├── requirements.txt     # Зависимости
├── .env.example        # Пример переменных окружения
├── alembic.ini         # Конфигурация Alembic
└── README.md           # Документация
```

## 🔧 API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| POST | `/tasks/` | Создать новую задачу |
| GET | `/tasks/` | Получить список задач |
| GET | `/tasks/{id}` | Получить задачу по ID |
| PUT | `/tasks/{id}` | Обновить задачу |
| DELETE | `/tasks/{id}` | Удалить задачу |
| GET | `/health` | Проверка здоровья API |

## 📝 Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.

## 🆘 Поддержка

Если у вас есть вопросы или проблемы, создайте issue в репозитории.

---

**Автор**: [Ваше имя]  
**Версия**: 1.0.0  
**Дата**: 2024

```

## 7. Дополнительные файлы для продакшена

```python:todo-api/app/config.py
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # База данных
    database_url: str = "sqlite:///./todo.db"
    
    # Настройки приложения
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    
    # CORS
    cors_origins: list = ["*"]
    
    # API
    api_v1_prefix: str = "/api/v1"
    project_name: str = "ToDo API"
    project_version: str = "1.0.0"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

Теперь у вас есть полноценный ToDo API проект! Вот что мы создали:

## ✅ Что готово:

1. **Структура проекта** - все файлы и папки организованы по лучшим практикам
2. **FastAPI приложение** - с роутами, моделями и схемами
3. **SQLAlchemy + Alembic** - для работы с БД и миграций
4. **Pydantic схемы** - для валидации данных
5. **CRUD операции** - полный набор операций с задачами
6. **Тесты** - покрытие всех основных функций
7. **CI/CD** - GitHub Actions для автоматического тестирования
8. **Документация** - подробный README с примерами

## 🎯 Что можно расширить:

- Аутентификация и авторизация
- Теги и категории для задач
- Приоритеты и дедлайны
- Поиск и фильтрация
- Пагинация
- Логирование
- Мониторинг
- Docker контейнеризация

Этот проект демонстрирует все ключевые навыки, которые ценят работодатели: архитектуру, работу с БД, тестирование, CI/CD и документацию!
