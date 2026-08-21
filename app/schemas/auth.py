
from pydantic import BaseModel, Field 

class UserCreate(BaseModel):
    username: str | None = None
    email: str = Field(description="Valid email address")
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str | None = None
    email: str

class UserMember(BaseModel):
    
    username: str | None = None

class userRole(BaseModel):
    role: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    