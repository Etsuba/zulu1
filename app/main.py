from fastapi import FastAPI
from app.routes import  tasks_router, auth_router

app = FastAPI()


# app.include_router(auth_router, prefix="/auth", tags=["Auth"])
# app.include_router(workspace_router, prefix="/workspaces", tags=["Workspaces"])
app.include_router(tasks_router, tags=["Tasks"])
app.include_router(auth_router, tags=["Auth"])