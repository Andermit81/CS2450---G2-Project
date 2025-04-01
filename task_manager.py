from task import Task
from taskstorage import TaskStorage

class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.tasks = {}  # {task_id: Task}
        return cls._instance

    def add_task(self, task: Task):
        if task.task_id in self.tasks:
            raise ValueError(f"Task with ID {task.task_id} already exists.")
        self.tasks[task.task_id] = task

    def remove_task(self, task_id: str):
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} does not exist.")
        del self.tasks[task_id]
        
    def save_tasks(self):
        TaskStorage().save_tasks(self.tasks)  

    def load_tasks(self):
        self.tasks = TaskStorage().load_tasks(self)

    def edit_task(self, task_id: str):
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} does not exist.")
        
        task = self.tasks[task_id]
        print(f"Editing Task: {task.title}")
        print(f"Leave fields blank to keep existing values.\n")

        # Getting user input for edits
        new_title = input(f"New Title ({task.title}): ").strip()
        new_description = input(f"New Description ({task.description}): ").strip()
        new_due_date = input(f"New Due Date ({task.due_date if task.due_date else 'N/A'}): ").strip()
        new_priority = input(f"New Priority ({task.priority}): ").strip()
        new_tags = input(f"New Tags (comma-separated) ({', '.join(task.tags) if task.tags else 'No tags'}): ").strip()

        # Updating fields if new values are provided
        if new_title:
            task.title = new_title
        if new_description:
            task.description = new_description
        if new_due_date:
            task.due_date = new_due_date
        if new_priority.lower() in ["high", "medium", "low"]:
            task.priority = new_priority.capitalize()
        if new_tags:
            task.tags = [tag.strip() for tag in new_tags.split(",")]

        print("Task updated successfully!")
        
