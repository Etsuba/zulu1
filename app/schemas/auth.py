
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str | None = None
    email: str
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
    