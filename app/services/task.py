# app/services/task.py
from app.repositories.task_repository import TaskRepository, task_repository
from app.schemas.tasks import TaskCreate, TaskUpdate


class TaskService:

  def __init__(self, repo: TaskRepository):
    self.repo = repo

  def create_task(self, task: TaskCreate) -> dict:
    task_data = task.model_dump()
    return self.repo.save(task_data)

  def get_task(self, task_id: int) -> dict | None:
    return self.repo.find_by_id(task_id)

  def list_tasks(self) -> list[dict]:
    return self.repo.find_all()

  def update_task(self, task_id: int, task_update: TaskUpdate) -> dict | None:
    update_data = task_update.model_dump(exclude_unset=True)
    return self.repo.update(task_id, update_data)

  def delete_task(self, task_id: int) -> bool:
    return self.repo.delete(task_id)


# Pass the instance into TaskService
task_service = TaskService(repo=task_repository)