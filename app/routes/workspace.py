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

@router.post("/workspace/{workspace_id}/members")
def add_member_to_workspace(workspace_id: int, member: dict):
    return {"message": f"Member added to workspace with ID {workspace_id}."}


@router.delete("/workspace/{workspace_id}/members/{member_id}")
def remove_member_from_workspace(workspace_id: int, member_id: int):
    return {"message": f"Member with ID {member_id} removed from workspace with ID {workspace_id}."}

@router.get("/workspace/{workspace_id}/members")
def list_workspace_members(workspace_id: int):
    return {"message": f"List of members in workspace with ID {workspace_id}."}

@router.post("/workspace/{workspace_id}/members/{member_id}/roles")
def add_role_to_member(workspace_id: int, member_id: int, role: str):
    return {"message": f"Role '{role}' added to member with ID {member_id} in workspace with ID {workspace_id}."}
