# from app.schemas.auth import UserMember
# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.schemas.workspace import WorkspaceCreate, WorkspaceResponse, WorkspaceUpdate

# workspace_router = APIRouter()

# @workspace_router.post("/workspace")
# def create_workspace(workspace: WorkspaceCreate):
#     return {"message": "Workspace created successfully."}

# @workspace_router.delete("/workspace/{workspace_id}")
# def delete_workspace(workspace_id: int):
#     return {"message": f"Workspace with ID {workspace_id} deleted successfully."}

# @workspace_router.get("/workspace/{workspace_id}")
# def get_workspace(workspace_id: int):
#     return {"message": f"Details of workspace with ID {workspace_id}."}

# @workspace_router.put("/workspace/{workspace_id}")
# def update_workspace(workspace_id: int, workspace: WorkspaceUpdate):
#     return {"message": f"Workspace with ID {workspace_id} updated successfully."}

# @workspace_router.post("/workspace/{workspace_id}/members")
# def add_member_to_workspace(workspace_id: int, member: UserMember):
#     return {"message": f"Member added to workspace with ID {workspace_id}."}


# @workspace_router.delete("/workspace/{workspace_id}/members/{user_id}")
# def remove_member_from_workspace(workspace_id: int, user_id: int):
#     return {"message": f"Member with ID {user_id} removed from workspace with ID {workspace_id}."}

# @workspace_router.get("/workspace/{workspace_id}/members")
# def list_workspace_members(workspace_id: int):
#     return {"message": f"List of members in workspace with ID {workspace_id}."}

# @workspace_router.post("/workspace/{workspace_id}/members/{user_id}/roles")
# def add_role_to_member(workspace_id: int, user_id: int, role: str):
#     return {"message": f"Role '{role}' added to member with ID {user_id} in workspace with ID {workspace_id}."}
