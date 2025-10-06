from sqlalchemy import Column, Integer, String, Text, DateTime, func
# func allows me to call SQL functions like now(), which we use for our created at column
from .database import Base # Task class inherits from Base, which we import from database.py

# we only have one model here
class Task(Base):
    __tablename__ = "tasks" #tells that tablename should be "tasks"

    id = Column(Integer, primary_key=True, index=True) #index = True lets SQLAlchemy create a database index on this column
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) # server default allows me to get current time if no data from Datetime is gotten

# Example Run:
# new_task = Task(title="Finish project", description="Due soon")
# session.add(new_task)
# session.commit()

# id not required in arguments because it is the primary key
# created_at not required because we have server_default
