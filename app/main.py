import sys
from repositories.json_repository import JSONTaskRepository
from services.task_service import TaskService
from views.task_view import TaskView
from controllers.task_controller import TaskController

def main() -> None:
    try:
        print("-"*50)
        print("Консольное приложение для управления списком дел")
        print("-"*50)
        
        repository = JSONTaskRepository()
        service = TaskService(repository)
        view = TaskView()
        controller = TaskController(service, view)
        controller.run()
        
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"\nErr: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()