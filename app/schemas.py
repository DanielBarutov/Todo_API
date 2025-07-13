from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Название задачи")
    description: Optional[str] = Field(None, max_length=1000, description="Описание задачи")
    is_completed: bool = Field(False, description="Статус выполнения задачи")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    is_completed: Optional[bool] = None

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 

class UserBase(BaseModel):
    username: str = Field(..., min_length=1, max_length=200, description="Имя пользователя")
    email: str = Field(..., min_length=1, max_length=200, description="Email пользователя")
    password: str = Field(..., min_length=1, max_length=200, description="Пароль пользователя")
    vacancy: Optional[str] = Field(None, max_length=200, description="Вакансия пользователя")

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 