from fastapi import APIRouter
from pydantic import BaseModel,Field
from app.schemas.auth import UserCreate,UserLogin,UserResponse

router = APIRouter()



@router.post("/Register")
def register_user(user: UserCreate):
    return {"message": f"User {user.username} registered successfully."}

@router.post("/Login")
def login_user(user: UserLogin):
    return {"message": f"User {user.username} logged in successfully."}

@router.get("/logout/")
def logout_user():
    return {"message": "User logged out successfully."}




