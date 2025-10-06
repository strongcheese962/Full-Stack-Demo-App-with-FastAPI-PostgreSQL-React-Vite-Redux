from sqlalchemy import select # select is needed for get tasks
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def get_tasks(session: AsyncSession):
    result = await session.execute(select(models.Task))
    tasks = result.scalars().all()
    return tasks

async def create_task(session: AsyncSession, task: schemas.TaskBase):
    new_task = models.Task(
        title=task.title,
        description=task.description
    )
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task

async def delete_task(session: AsyncSession, task_id: int):
    task = await session.get(models.Task, task_id)
    if task is None:
        return False
    await session.delete(task)
    await session.commit()
    return True










