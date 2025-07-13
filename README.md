### I am Danil Barutov, an aspiring Python backend developer.  
I self-studied a modern Python web development stack (FastAPI, SQLAlchemy, Alembic, Pydantic, Pytest, and GitHub Actions) in an intensive seven-day period and built a ToDo REST API project to demonstrate my skills.  
Despite having no formal industry experience, I have completed this case project and undertaken freelance development work.  
I am passionate about backend development and continuously learning to improve my skills.  

## Case Project: ToDo REST API


**Project Title**: ToDo REST API  

**Objective**: Develop a complete RESTful API for managing a to-do list, demonstrating proficiency in backend development and best practices.  

**Architecture**: The project uses a modular architecture with separate modules for database models, API routes, and data schemas. It includes SQLAlchemy models for database interactions, Pydantic schemas for input/output validation, and Alembic for database migrations.  

**Tech Stack**: FastAPI (web framework), SQLAlchemy (ORM), Alembic (database migrations), Pydantic (data validation), Pytest (testing), Git & GitHub Actions (version control and CI/CD).  

**Key Components**: CRUD API endpoints for task management, proper data validation and error handling, database migrations, and automated tests.   


### GitHub: [Todo_API](https://github.com/DanielBarutov/Todo_API)

## Contact Information

**Name**: Danil Barutov  
**Email**: barutovdg@gmail.com  
**Telegram**: @daniel_papo  
**GitHub**: [github.com/danilbarutov](https://github.com/DanielBarutov)


## 🚀 Features

- ✅ CRUD operations for tasks
- 🗄️ SQLAlchemy ORM with migration support
- 📚 Automatic API documentation (Swagger/ReDoc)
- 🗄️ SQLAlchemy ORM with migration support

## 🛠️ Technology stack

- **FastAPI** - a modern web framework for Python
- **SQLAlchemy** - ORM for working with the database
- **Alembic** - migration system
- **Pydantic** - data validation
- **Pytest** - testing
- **SQLite** - database (can be replaced with PostgreSQL)

## 🛠️ Technology stack

### Preliminary requirements

- Python 3.9+
- pip

### Local installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd todo-api
```

2. **Create a virtual environment:**
``bash
python -m venv venv
source venv/bin/activate # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure the environment variables:**
```bash
cp .env.example .env
# Edit it .env file if necessary
``

5. **Start migrations:**
```bash
alembic upgrade head
```

6. **Start the server:**
```bash
uvicorn app.main:app --reload
```

The API will be available at: http://localhost:8000

# 📚 Automatic API Documentation (Swagger/ReDoc)

After starting the server, the documentation is available at the following addresses:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testing

### Running tests
```bash
pytest tests/ -v
```

### Running tests with coverage
```bash
pytest tests/ -v --cov=app --cov-report=html
```

## 📋 Usage examples

### Creating a task
```bash
curl -X POST "http://localhost:8000/tasks/" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Explore FastAPI",
"description": "Explore documentation and create the first project",
       "is_completed": false
     }'
```

### Getting the task list
```bash
curl -X GET "http://localhost:8000/tasks/"
```

### Getting a specific task
```bash
curl -X GET "http://localhost:8000/tasks/1"
```

### Updating the task
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Explore FastAPI (updated)",
       "is_completed": true
     }'
```

### Deleting an issue
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

## 📋 Usage examples

## 📋 Usage examples

```
todo-api/
├── app/
│   ├── __init__.py
│   ├── main.py # Application Entry Point
│   ├── models.py # SQLAlchemy models
│   ├── schemas.py # Pydantic schemes
│   ├── crud.py # CRUD operations
│   ├── routes.py        # API endpoints
│   └── database.py # Database Configuration
├── alembic/ # Database migrations
├── tests/               # Tests
,──__
init__.py ,── conftest.py # Pytest configuration
,── test_tasks.py # Tests for tasks
├── .github/workflows/ # CI/CD
├── requirements.txt # Dependencies
├── .env.example # Example of environment variables
,── alembic.ini # Alembic configuration
,── README.md # Documentation
```

## 🔧 API Endpoints

| The | Endpoint | method Description |
|-------|----------|----------|
| POST | `/tasks/` | Create a new task |
| GET | `/tasks/` | Get a list of tasks |
| GET | `/tasks/{id}` | Get a task by ID |
|PUT | `/tasks/{id}` | Update the issue |
| DELETE | `/tasks/{id}` | Delete an issue |
| POST | `/user/` | Create a new user |
| GET | `/users/` | Get a list of users |
| GET | `/health` | API Health Check |


## 🆘 Support

If you have any questions or concerns, create an issue in the repository.

---

**Author**: Danil Barutov  
**Version**: 1.0.0  
**Date**: 2025

```
