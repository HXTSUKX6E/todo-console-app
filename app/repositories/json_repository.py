import json
import os
from typing import List, Optional
from models.task import Task
from .base import TaskRepository

class JSONTaskRepository(TaskRepository):
    
    def __init__(self, filename: str = "todo_list.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load()
    
    def load(self) -> None:
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
                    if self.tasks:
                        self.next_id = max(task.id for task in self.tasks) + 1
                print(f"Загружено {len(self.tasks)} задач из {self.filename}")
            else:
                self.tasks = []
                print("Создан новый список задач")
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при загрузке файла: {e}")
            self.tasks = []
    
    def save(self) -> None:
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([task.to_dict() for task in self.tasks], 
                         file, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"Ошибка при сохранении файла: {e}")
    
    def get_all(self) -> List[Task]:
        return self.tasks.copy()
    
    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def add(self, task: Task) -> None:
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        self.save()
    
    def update(self, task: Task) -> None:
        for i, existing_task in enumerate(self.tasks):
            if existing_task.id == task.id:
                self.tasks[i] = task
                self.save()
                return
    
    def delete(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self.save()
                return True
        return False