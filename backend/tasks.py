from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from .database import SessionLocal
from . import crud, schemas

router = APIRouter()

@router.get("/tasks", response_model=list[schemas.TaskResponse])
async def read_tasks():
    async with SessionLocal() as session:
        return await crud.get_tasks(session)

@router.post("/tasks", response_model=schemas.TaskResponse)
async def create_task(task: schemas.TaskBase):
    async with SessionLocal() as session:
        return await crud.create_task(session, task)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    async with SessionLocal() as session:
        deleted = await crud.delete_task(session, task_id)
        return {"success": deleted}


