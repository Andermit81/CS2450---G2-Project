from task import Task
import json

class TaskStorage():
    def save_tasks(self, tasks):
        tasks_dict = {}
        for task_id in tasks:
            target_task = tasks[task_id] 
            tasks_dict[task_id] = [target_task.title, target_task.description, target_task.due_date, target_task.priority, target_task.tags]
        with open("tasklist.json", 'w') as tasks_file:
            json.dump(tasks_dict, tasks_file)
        print("Tasks saved successfully!")

    def load_tasks(self, task_man):
        try:
            with open("tasklist.json", 'r') as tasks_file:
                tasks_dict = json.load(tasks_file)
                for task_id, task_data in tasks_dict.items():
                    added_task = Task(task_data[0])
                    added_task.task_id = task_id
                    added_task.description = task_data[1]
                    added_task.due_date = task_data[2]
                    added_task.priority = task_data[3]
                    added_task.tags = task_data[4]
                    task_man.tasks[task_id] = added_task
                print("Tasks loaded successfully!")
                return task_man.tasks 
        except FileNotFoundError:
            print("No saved tasks found.")
            return {}
