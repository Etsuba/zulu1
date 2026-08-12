

from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    due-date: str | None = None
    assigned_to: str | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    due-date: str | None = None
    assigned_to: str | None = None

class TaskResponse(BaseModel):  
    id: int
    title: str
    description: str | None = None
    due-date: str | None = None
    assigned_to: str | None = None
    workspace_id: int