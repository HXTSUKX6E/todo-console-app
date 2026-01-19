from services.task_service import TaskService
from views.task_view import TaskView
from validators.input_validator import InputValidator

class TaskController:
    
    def __init__(self, service: TaskService, view: TaskView):
        self.service = service
        self.view = view
        self.validator = InputValidator()
    
    def show_all_tasks(self) -> None:
        """Показать все задачи"""
        tasks = self.service.get_all_tasks()
        pending = self.service.get_pending_tasks()
        completed = self.service.get_completed_tasks()
        
        self.view.display_task_list(tasks, "ВСЕ ЗАДАЧИ")
        self.view.display_statistics(len(pending), len(completed))
    
    def show_pending_tasks(self) -> None:
        tasks = self.service.get_pending_tasks()
        self.view.display_task_list(tasks, "Список невыполненных зачад")
        self.view.display_statistics(len(tasks), 0)
    
    def show_completed_tasks(self) -> None:
        tasks = self.service.get_completed_tasks()
        self.view.display_task_list(tasks, "Список выполненных зачад")
        self.view.display_statistics(0, len(tasks))
    
    def add_task(self) -> None:
        print("\n" + "-"*50)
        print("ДОБАВЛЕНИЕ НОВОЙ ЗАДАЧИ")
        print("-"*50)
        
        while True:
            title = input("Введите название задачи: ").strip()
            if self.validator.validate_non_empty(title):
                break
            self.view.display_message("Название задачи не может быть пустым!", is_error=True)
            print("Пожалуйста, введите название заново.\n")
        
        description = input("Введите описание задачи (необязательное поле): ").strip()
        
        while True:
            due_date = input("Введите срок выполнения (ДД.ММ.ГГГГ) или оставьте пустым: ").strip()
            if not due_date:
                break
            if self.validator.validate_date(due_date):
                break
            self.view.display_message("Неверный формат даты! Используйте ДД.ММ.ГГГГ", is_error=True)
            print("Пример: 25.12.2024\n")
        
        try:
            task = self.service.create_task(title, description, due_date)
            self.view.display_message(f"Задача добавлена! (ID: {task.id})")
        except ValueError as e:
            self.view.display_message(str(e), is_error=True)
    
    def delete_task(self) -> None:
        tasks = self.service.get_all_tasks()
        if not tasks:
            self.view.display_message("Список задач пуст! Нечего удалять.", is_error=True)
            return
        
        self.show_all_tasks()
        
        print("\n" + "-"*50)
        print("УДАЛЕНИЕ ЗАДАЧИ")
        print("-"*50)
        
        while True:
            task_id_input = input("Введите ID задачи для удаления (или 0 для отмены): ").strip()
            
            if task_id_input == "0":
                self.view.display_message("Удаление отменено.")
                return
            
            task_id = self.validator.validate_task_id(task_id_input)
            
            if task_id:
                break
            self.view.display_message("Неверный формат ID! Введите целое положительное число.", is_error=True)
            print("Пример: 1, 2, 3\n")
        
        if self.service.delete_task(task_id):
            self.view.display_message(f"Задача с ID {task_id} удалена!")
        else:
            self.view.display_message(f"Задача с ID {task_id} не найдена!", is_error=True)
    
    def complete_task(self) -> None:
        pending_tasks = self.service.get_pending_tasks()
        if not pending_tasks:
            self.view.display_message("Нет невыполненных задач!", is_error=True)
            return
        
        self.show_pending_tasks()
        
        print("\n" + "-"*50)
        print("ОТМЕТКА ЗАДАЧИ КАК ВЫПОЛНЕННОЙ")
        print("-"*50)
        
        while True:
            task_id_input = input("Введите ID выполненной задачи (или 0 для отмены): ").strip()
            
            if task_id_input == "0":
                self.view.display_message("Действие отменено.")
                return
            
            task_id = self.validator.validate_task_id(task_id_input)
            
            if task_id:
                break
            self.view.display_message("Неверный формат ID! Введите целое положительное число.", is_error=True)
            print("Пример: 1, 2, 3\n")
        
        if self.service.complete_task(task_id):
            self.view.display_message(f"Задача с ID {task_id} отмечена как выполненная!")
        else:
            all_tasks = self.service.get_all_tasks()
            task_exists = any(t.id == task_id for t in all_tasks)
            if task_exists:
                self.view.display_message("Эта задача уже отмечена как выполненная!", is_error=True)
            else:
                self.view.display_message(f"Задача с ID {task_id} не найдена!", is_error=True)
    
    def run(self) -> None:
        while True:
            print("\n" + "="*50)
            print("ГЛАВНОЕ МЕНЮ:")
            print("="*50)
            print("1. Показать все задачи")
            print("2. Добавить задачу")
            print("3. Удалить задачу")
            print("4. Отметить задачу как выполненную")
            print("5. Показать только невыполненные задачи")
            print("6. Показать только выполненные задачи")
            print("7. Выход")
            print("="*50)
            
            while True:
                choice = input("Выберите действие (1-7): ").strip()
                if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                    break
                self.view.display_message("Неверный выбор! Пожалуйста, введите число от 1 до 7", is_error=True)
                print("Попробуйте еще раз.\n")
            
            if choice == "1":
                self.show_all_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.complete_task()
            elif choice == "5":
                self.show_pending_tasks()
            elif choice == "6":
                self.show_completed_tasks()
            elif choice == "7":
                print("\n" + "="*60)
                print("Спасибо за использование приложения! До свидания!")
                print("="*60)
                break