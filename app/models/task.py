from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional
from .task_status import TaskStatus

@dataclass
class Task:
    """Модель задачи"""
    id: int
    title: str
    description: str = ""
    due_date: str = ""
    status: TaskStatus = TaskStatus.PENDING
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%d.%m.%Y %H:%M"))
    completed_at: Optional[str] = None
    
    def mark_completed(self) -> None:
        self.status = TaskStatus.COMPLETED
        self.completed_at = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    def to_dict(self) -> dict:
        data = asdict(self)
        data['status'] = self.status.value
        if self.completed_at is None:
            data.pop('completed_at', None)
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        # Создание копии
        task_data = data.copy()
        task_data['status'] = TaskStatus(task_data['status'])
        return cls(**task_data)