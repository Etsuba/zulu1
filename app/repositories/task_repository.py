class TaskRepository:

  def __init__(self):
    self._tasks_db: dict[int, dict] = {}
    self._next_id: int = 1

  def save(self, task_data: dict) -> dict:
    task_id = self._next_id
    self._next_id += 1

    task_data["id"] = task_id
    self._tasks_db[task_id] = task_data
    return task_data

  def find_by_id(self, task_id: int) -> dict | None:
    return self._tasks_db.get(task_id)

  # def find_all(self) -> list[dict]:
  #   return list(self._tasks_db.values())

  def update(self, task_id: int, update_data: dict) -> dict | None:
    task = self.find_by_id(task_id)
    if not task:
      return None

    task.update(update_data)
    return task

  def delete(self, task_id: int) -> bool:
    if task_id in self._tasks_db:
      del self._tasks_db[task_id]
      return True
    return False



task_repository = TaskRepository()