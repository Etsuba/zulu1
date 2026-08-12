from fastapi import APIRouter
from pydantic import BaseModel,Field

router = APIRouter()

class User(BaseModel):
    username: str | None = None
    email: str
    password: str=Field(min_length=8, max_length=20, description="Password must be between 8 and 20 characters long.")

@router.post("/Register")
def register_user(user:User):
    return {"message": f"User {user.username} registered successfully."}

@router.post("/Login")
def login_user(user:User):
    return {"message": f"User {user.username} logged in successfully."}

@router.get("/logout")
def logout_user():
    return {"message": "User logged out successfully."}




