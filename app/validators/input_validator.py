from datetime import datetime

class InputValidator:
    @staticmethod
    def validate_task_id(input_str: str) -> int | None:
        """Валидация ID задачи"""
        try:
            task_id = int(input_str.strip())
            return task_id if task_id > 0 else None
        except ValueError:
            return None
    
    @staticmethod
    def validate_date(date_str: str) -> bool:
        """Валидация даты"""
        try:
            datetime.strptime(date_str.strip(), "%d.%m.%Y")
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_non_empty(text: str) -> bool:
        """Проверка, что строка не пустая"""
        return bool(text.strip())