import json

class Task:
    id = 0
    def __init__(self, name):
        self.name = name
        self.completed = False
        self.id = Task.id
        Task.id += 1
        
    def mark_done(self):
        self.completed = True
    
class TaskList:
    def __init__(self):
        self.tasks = {}
    
    def save(self):
        task_json = json.dumps(self.tasks)
        with open("tasklist.json", 'w') as tasks:
            tasks.writelines(task_json)
    
    def load(self):
        with open("tasklist.json", 'r') as tasks:
            task_dict = tasks.readlines()
            self.tasks = json.loads(task_dict)