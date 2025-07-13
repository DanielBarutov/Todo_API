from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .routes import router, routerUsers
from .database import engine
from . import models

# Создаем таблицы в базе данных
models.Base.metadata.create_all(bind=engine)

# Создаем экземпляр FastAPI
app = FastAPI(
    title="ToDo API",
    description="API для управления задачами с использованием FastAPI и SQLAlchemy",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене указать конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роуты
app.include_router(router)
app.include_router(routerUsers)
app.mount("/public", StaticFiles(directory="app/public"), name="public")
@app.get("/")
def create_page():
    return {"message": "ToDo API, version 1.0.0"}



@app.get("/health")
def health_check():
    """
    Проверка здоровья API
    """
    return {"status": "healthy"} 