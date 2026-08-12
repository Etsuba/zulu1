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

