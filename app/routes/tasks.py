from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.tasks import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter()
    
@router.post("/workspace/{workspace_id}/tasks")
def create_task(workspace_id: int, task: TaskCreate):
    return {"message": f"Task '{task.title}' created successfully."}



@router.delete("/workspace/{workspace_id}/tasks/{task_id}")
def delete_task(workspace_id: int, task_id: int):
    return {"message": f"Task with ID {task_id} deleted successfully."}


 
@router.get("/workspace/{workspace_id}/tasks/{task_id}")
def get_task(workspace_id: int, task_id: int):
    return {"message": f"Details of task with ID {task_id}."}


@router.put("/workspace/{workspace_id}/tasks/{task_id}")
def update_task(workspace_id: int, task_id: int, task: TaskUpdate):
    return {"message": f"Task with ID {task_id} updated successfully."}


