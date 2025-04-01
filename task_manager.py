from task import Task
from taskstorage import TaskStorage 
import json

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
        
        TaskEditor.edit(task) 
