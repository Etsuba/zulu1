from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Workspace(BaseModel):
    name: str
    description: str | None = None

@router.post("/workspace")
def create_workspace(workspace: Workspace):
    return {"message": "Workspace created successfully."}

@router.delete("/workspace/{workspace_id}")
def delete_workspace(workspace_id: int):
    return {"message": f"Workspace with ID {workspace_id} deleted successfully."}

@router.get("/workspace/{workspace_id}")
def get_workspace(workspace_id: int):
    return {"message": f"Details of workspace with ID {workspace_id}."}

@router.put("/workspace/{workspace_id}")
def update_workspace(workspace_id: int, workspace: Workspace):
    return {"message": f"Workspace with ID {workspace_id} updated successfully."}

@router.post("/workspace/{workspace_id}/task")
def add_item_to_workspace(workspace_id: int, task: dict[str, str]):
    return {"message": f"Task added to workspace with ID {workspace_id}."}

@router.delete("/workspace/{workspace_id}/task/{task_id}")
def remove_item_from_workspace(workspace_id: int, task_id: int):
    return {"message": f"Task with ID {task_id} removed from workspace with ID {workspace_id}."}

@router.get("/workspace/{workspace_id}/task/{task_id}")
def get_item_from_workspace(workspace_id: int, task_id: int):
    return {"message": f"Details of task with ID {task_id} in workspace with ID {workspace_id}."}





