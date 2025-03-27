from task import Task
import json

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
         
    def view_tasks(self):
        if not self.tasks:
            return "No tasks available."
        output = f"{'Task ID':<36} | {'Title':<20} | {'Priority':<10} | {'Due Date':<15} | {'Tags':<30}\n"
        output += "-" * 90 + "\n"


        for task in self.tasks.values():  
            tags_str = ", ".join(sorted(task.tags)) if task.tags else "No tags"
            output += f"{task.task_id:<36} | {task.title:<20} | {task.priority:<10} | {task.due_date if task.due_date else 'N/A':<15} | {tags_str:<30}\n"

        return output  # Returns the table as a string
        
    def save_tasks(self):
        tasks_dict = {}
        for task_id in self.tasks:
            target_task = self.tasks[task_id]
            tasks_dict[task_id] = [target_task.title, target_task.description, target_task.due_date, target_task.priority, target_task.tags]
        task_json = json.dumps(tasks_dict)
        with open("tasklist.json", 'w') as tasks_file:
            tasks_file.writelines(task_json)
        print("Tasks saved!")
    
    def load_tasks(self):
        try:
            with open("tasklist.json", 'r') as tasks_file:
                task_json = tasks_file.read()
                tasks_dict = json.loads(task_json)
                self.tasks = {}
                for taskitem_id in tasks_dict.keys():
                    added_task = Task(tasks_dict[taskitem_id][0])
                    added_task.task_id = taskitem_id
                    added_task.description = tasks_dict[taskitem_id][1]
                    added_task.due_date = tasks_dict[taskitem_id][2]
                    added_task.priority = tasks_dict[taskitem_id][3]
                    added_task.tags = tasks_dict[taskitem_id][4]
                    self.tasks[taskitem_id] = added_task
            print("Tasks loaded successfully!")
        except:
            print("No tasks found, are you sure a tasklist.json exists?")
