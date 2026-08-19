from fastapi import APIRouter, HTTPException, status    
from pydantic import BaseModel,Field
from app.schemas.auth import UserCreate,UserLogin,UserResponse
from app.services.auth import user_service

auth_router = APIRouter()



@auth_router.post("/Register", response_model= UserResponse, status_code=status.HTTP_201_CREATED,)
def register_user(user: UserCreate):
    return user_service.create_user(user)

@auth_router.post("/Login")
def login_user(user: UserLogin):
    return {"message": f"User {user.username} logged in successfully."}

@auth_router.get("/logout/")
def logout_user():
    return {"message": "User logged out successfully."}




