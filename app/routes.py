from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import crud, schemas, database

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    """
    Создать новую задачу
    """
    return crud.TaskCRUD.create_task(db=db, task=task)

@router.get("/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """
    Получить список задач с пагинацией
    """
    tasks = crud.TaskCRUD.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(database.get_db)):
    """
    Получить задачу по ID
    """
    task = crud.TaskCRUD.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(database.get_db)):
    """
    Обновить задачу
    """
    task = crud.TaskCRUD.update_task(db, task_id=task_id, task_update=task_update)
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    """
    Удалить задачу
    """
    success = crud.TaskCRUD.delete_task(db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Задача не найдена") 
# Роуты для пользователей
routerUsers = APIRouter(prefix="/users", tags=["users"])

@routerUsers.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """
    Создать нового пользователя
    """
    return crud.UserCRUD.create_user(db=db, user=user)
@routerUsers.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """
    Получить список пользователей с пагинацией
    """
    users = crud.UserCRUD.get_users(db, skip=skip, limit=limit)
    return users