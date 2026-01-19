from abc import ABC, abstractmethod
from typing import List, Optional
from models.task import Task

class TaskRepository(ABC):
    """Абстрактный репозиторий"""
    
    @abstractmethod
    def get_all(self) -> List[Task]:
        """Получить все задачи"""
        pass
    
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Получить задачу по ID"""
        pass
    
    @abstractmethod
    def add(self, task: Task) -> None:
        """Добавить новую задачу"""
        pass
    
    @abstractmethod
    def update(self, task: Task) -> None:
        """Обновить задачу"""
        pass
    
    @abstractmethod
    def delete(self, task_id: int) -> bool:
        """Удалить задачу по ID"""
        pass
    
    @abstractmethod
    def save(self) -> None:
        """Сохранить изменения"""
        pass