from pydantic import BaseModel, ConfigDict
from datetime import datetime




class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)



