# app/routes/tasks.py
from app.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate
from app.services.task import task_service
from fastapi import APIRouter, HTTPException, status

tasks_router = APIRouter()


@tasks_router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task: TaskCreate):
  return task_service.create_task(task)


@tasks_router.get("/tasks", response_model=list[TaskResponse])
def list_all_tasks():
  return task_service.list_tasks()


@tasks_router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
  task = task_service.get_task(task_id)
  if not task:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
    )
  return task


@tasks_router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
  updated_task = task_service.update_task(task_id, task)
  if not updated_task:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Task not found to update"
    )
  return updated_task


@tasks_router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
  deleted = task_service.delete_task(task_id)
  if not deleted:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Task not found to be deleted"
    )
  return {"message": f"Task with ID {task_id} deleted successfully"}