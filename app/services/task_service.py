from datetime import datetime
from typing import List, Tuple
from models.task import Task
from repositories.base import TaskRepository

class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository
    
    def create_task(self, title: str, description: str = "", due_date: str = "") -> Task:
        if not title.strip():
            raise ValueError("Название задачи не может быть пустым!")
        
        if due_date:
            try:
                datetime.strptime(due_date, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Неверный формат даты! Используйте ДД.ММ.ГГГГ")
        
        task = Task(
            id=0,  # из репозитория
            title=title.strip(),
            description=description.strip(),
            due_date=due_date.strip()
        )
        
        self.repository.add(task)
        return task
    
    def complete_task(self, task_id: int) -> bool:
        task = self.repository.get_by_id(task_id)
        if not task:
            return False
        
        if task.status.value == "completed":
            return False  # флаг - выполнена
        
        task.mark_completed()
        self.repository.update(task)
        return True
    
    def delete_task(self, task_id: int) -> bool:
        return self.repository.delete(task_id)
    
    def get_all_tasks(self) -> List[Task]:
        return self.repository.get_all()
    
    def get_pending_tasks(self) -> List[Task]:
        return [task for task in self.repository.get_all() 
                if task.status.value == "pending"]
    
    def get_completed_tasks(self) -> List[Task]:
        return [task for task in self.repository.get_all() 
                if task.status.value == "completed"]
    
    def get_task_statistics(self) -> Tuple[int, int]:
        all_tasks = self.repository.get_all()
        pending = len([t for t in all_tasks if t.status.value == "pending"])
        completed = len([t for t in all_tasks if t.status.value == "completed"])
        return pending, completed
    
    def is_empty(self) -> bool:
        return len(self.repository.get_all()) == 0