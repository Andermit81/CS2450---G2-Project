from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}  # {task_id: Task}

    def add_task(self, task: Task):
        if task.task_id in self.tasks:
            raise ValueError(f"Task with ID {task.task_id} already exists.")
        self.tasks[task.task_id] = task

    def remove_task(self, task_id: str):
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} does not exist.")
        del self.tasks[task_id]