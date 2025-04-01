from task import Task
from task_manager import TaskManager
import json

class TaskStorage():
    def save_tasks(self, tasks):
        tasks_dict = {}
        for task_id in tasks:
            target_task = self.tasks[task_id]
            tasks_dict[task_id] = [target_task.title, target_task.description, target_task.due_date, target_task.priority, target_task.tags]
        task_json = json.dumps(tasks_dict)
        with open("tasklist.json", 'w') as tasks_file:
            tasks_file.writelines(task_json)
        print("Tasks saved!")
    
    def load_tasks(self, task_man):
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
                    task_man.tasks[taskitem_id] = added_task
            print("Tasks loaded successfully!")
        except:
            print("No tasks found, are you sure a tasklist.json exists?")