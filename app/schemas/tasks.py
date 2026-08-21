

from pydantic import BaseModel, fields



class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    due_date: str | None = None
    assigned_to: str | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    due_date: str | None = None
    assigned_to: str | None = None

class TaskResponse(TaskCreate):  
    id: int
    # workspace_id: int