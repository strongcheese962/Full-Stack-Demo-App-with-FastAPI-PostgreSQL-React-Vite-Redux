from sqlalchemy import select # select is needed for get tasks
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

#COROUTINE: an async method that does not return the object right away
#For us, we need the database to respond

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
    # we need to await both commit and refresh because we are loading awaitable objects
    # it asks to do something with the DB, then return to finish
    await session.commit() # this awaits for confirmation that changes are made, wait until DB says the write is finished
    await session.refresh(new_task) # needs to wait until DB sends back updated row
    return new_task

async def delete_task(session: AsyncSession, task_id: int):
    task = await session.get(models.Task, task_id) # must await since get is a , wait for database to respond with either row (as Task object) or None
    if task is None:
        return False
    await session.delete(task)
    await session.commit()
    return True










