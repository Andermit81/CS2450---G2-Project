from .task_manager import TaskManager
from .task import Task

class ActionQueue:
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ActionQueue, cls).__new__(cls)
            cls._instance._undo_queue = []
            cls._instance._redo_queue = []
            cls._instance._task_man_instance = TaskManager()
        return cls._instance 
    
    '''   
        def __init__(self):
        self._undo_queue = []
        self._redo_queue = []
        self._task_man_instance = TaskManager()
    '''
        
    def add_action(self, restore_item, action: str):
        self._undo_queue.append([restore_item, action])
        
    def undo_action(self):
        action_item = self._undo_queue.pop()
        self._redo_queue.append(action_item)
        
        if len(self._undo_queue) == 0:
            print("Nothing to undo")
            return
        
        if action_item[1] == "add":
            self._task_man_instance.remove_task(action_item[0])
        
        elif action_item[1] == "delete":
            self._task_man_instance.add_task(action_item[0])
            
        elif action_item[1] == "edit":
            self._redo_queue[-1][0] = self._task_man_instance.tasks[action_item[0].id]
            self._task_man_instance.tasks[action_item[0].id] = action_item[0]
        
        elif action_item[1] == "sort":
            self._redo_queue[-1][0] = self._task_man_instance.tasks
            self._task_man_instance.tasks = action_item[0]
        
    def redo_action(self):
        action_item = self._redo_queue.pop()
        self._undo_queue.append(action_item)
        
        if len(self._redo_queue) == 0:
            print("Nothing to redo")
            return
        
        if action_item[1] == "add":
            self._task_man_instance.add_task(action_item[0])
        
        elif action_item[1] == "delete":
            self._task_man_instance.remove_task(action_item[0])
        
        elif action_item[1] == "edit":
            self._undo_queue[-1][0] = self._task_man_instance.tasks[action_item[0].id]
            self._task_man_instance.tasks[action_item[0].id] = action_item[0]
        
        elif action_item[1] == "sort":
            self._undo_queue[-1][0] = self._task_man_instance.tasks
            self._task_man_instance.tasks = action_item[0]
         