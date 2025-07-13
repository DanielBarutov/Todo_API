from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas


class TaskCRUD:
    @staticmethod
    def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
        db_task = models.Task(**task.model_dump())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    @staticmethod
    def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[models.Task]:
        return db.query(models.Task).offset(skip).limit(limit).all()

    @staticmethod
    def get_task(db: Session, task_id: int) -> Optional[models.Task]:
        return db.query(models.Task).filter(models.Task.id == task_id).first()

    @staticmethod
    def update_task(
        db: Session, task_id: int, task_update: schemas.TaskUpdate
    ) -> Optional[models.Task]:
        db_task = TaskCRUD.get_task(db, task_id)
        if db_task:
            update_data = task_update.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_task, field, value)
            db.commit()
            db.refresh(db_task)
        return db_task

    @staticmethod
    def delete_task(db: Session, task_id: int) -> bool:
        db_task = TaskCRUD.get_task(db, task_id)
        if db_task:
            db.delete(db_task)
            db.commit()
            return True
        return False


class UserCRUD:
    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate) -> models.User:
        db_user = models.User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
        return db.query(models.User).offset(skip).limit(limit).all()
