from fastapi import APIRouter, HTTPException, status    
from pydantic import BaseModel,Field
from app.schemas.auth import UserCreate,UserLogin,UserResponse,UserMember,userRole,UserUpdate
from app.services.auth import user_service

auth_router = APIRouter()



@auth_router.post("/Register", response_model= UserResponse, status_code=status.HTTP_201_CREATED,)
def register_user(user: UserCreate):
    return user_service.create_user(user)

# @auth_router.post("/Login", response_model = UserLogin, status_code=status.HTTP_200_OK)
# def login_user(user: UserLogin):

#     return {"message": f"User {user.username} logged in successfully."}

@auth_router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = user_service.get_auth(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found here")
    return user

@auth_router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate):
    updated_user = user_service.update_auth(user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found to be updated")
    return updated_user


@auth_router.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted = user_service.delete_auth(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found to be deleted")
    return {"message": f"User with ID {user_id} deleted successfully."}


# @auth_router.get("/logout/")
# def logout_user():
#     return {"message": "User logged out successfully."}






