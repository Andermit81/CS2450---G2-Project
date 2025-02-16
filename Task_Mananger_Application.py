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