import asyncio
from .database import SessionLocal
from . import crud, schemas

async def main():
    # Create a new session
    async with SessionLocal() as session:
        # 1. Create a new task
        new_task = await crud.create_task(
            session,
            schemas.TaskBase(title="Test Task", description="Check if CRUD works")
        )
        print("Created:", new_task.id, new_task.title, new_task.description)

        # 2. Get all tasks
        tasks = await crud.get_tasks(session)
        print("Tasks in DB:")
        for t in tasks:
            print(t.id, t.title, t.description)

        # 3. Delete the task we just made
        deleted = await crud.delete_task(session, new_task.id)
        print("Deleted?", deleted)

# Run it
asyncio.run(main())

