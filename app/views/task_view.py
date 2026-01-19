from typing import List
from models.task import Task

class TaskView:
    
    @staticmethod
    def display_task(task: Task) -> str:
        status_icon = "✓" if task.status.value == "completed" else "□"
        due_info = f" | Срок: {task.due_date}" if task.due_date else ""
        
        output = f"ID: {task.id:3} | {status_icon} {task.title}{due_info}"
        
        if task.description:
            output += f"\n Описание: {task.description}"
        
        output += f"\n Создано: {task.created_at}"
        
        if task.status.value == "completed" and task.completed_at:
            output += f"\n      ✅ Выполнено: {task.completed_at}"
        
        return output
    
    @staticmethod
    def display_task_list(tasks: List[Task], title: str = "ЗАДАЧИ") -> None:
        if not tasks:
            print(f"\n{'='*80}")
            print(f"{title}: СПИСОК ПУСТ")
            print('='*80)
            return
        
        print(f"\n{'-'*80}")
        print(title)
        print('-'*80)
        
        for task in tasks:
            print(TaskView.display_task(task))
            print("-"*80)
    
    @staticmethod
    def display_statistics(pending_count: int, completed_count: int) -> None:
        """Отобразить статистику"""
        if pending_count == 0 and completed_count == 0:
            print(f"\n📊 Статистика: список задач пуст")
        else:
            print(f"\n📊 Статистика: {pending_count} невыполненных, {completed_count} выполненных")
    
    @staticmethod
    def display_message(message: str, is_error: bool = False) -> None:
        """Отобразить сообщение"""
        prefix = "❌" if is_error else "✓"
        print(f"\n{prefix} {message}")