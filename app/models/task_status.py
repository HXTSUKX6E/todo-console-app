from enum import Enum

class TaskStatus(Enum):
    """Статусы задач"""
    PENDING = "pending"
    COMPLETED = "completed"