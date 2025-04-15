from .task_manager import TaskManager
from .task import Task

'''An action queue that keeps track of actions completed and then puts them in a queue.
These actions can then later be undone or redone.'''


class ActionQueue:
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ActionQueue, cls).__new__(cls)
            cls._undo_queue = []
            cls._redo_queue = []
            cls._task_man_instance = TaskManager()
        return cls._instance   
    '''
    def __init__(self):
        self._undo_queue = []
        self._redo_queue = []
        self._task_man_instance = TaskManager()
    '''
    #Every time an undoable action is performed, this should be called immediately after.
    @classmethod    
    def add_action(cls, restore_item, action: str):
        ActionQueue._undo_queue.append([restore_item, action])
        print("Adding action")
    
    #Undoes the latest action. Right now only works with add/delete.  
    @classmethod    
    def undo_action(cls):
        action_item = ActionQueue._undo_queue.pop()
        ActionQueue._redo_queue.append(action_item)
        
        if len(ActionQueue._undo_queue) < 0:
            print("Nothing to undo")
            return
        
        if action_item[1] == "add":
            ActionQueue._task_man_instance.remove_task(action_item[0].task_id)
        
        elif action_item[1] == "delete":
            ActionQueue._task_man_instance.add_task(action_item[0])
            
        elif action_item[1] == "edit":
            ActionQueue._redo_queue[-1][0] = ActionQueue._task_man_instance.tasks[action_item[0].task_id]
            ActionQueue._task_man_instance.tasks[action_item[0].task_id] = action_item[0]
        
        elif action_item[1] == "sort":
            ActionQueue._redo_queue[-1][0] = ActionQueue._task_man_instance.tasks
            ActionQueue._task_man_instance.tasks = action_item[0]
    
    #Redoes the latest action. As of now, only add/delete work.
    @classmethod    
    def redo_action(cls):
        action_item = ActionQueue._redo_queue.pop()
        ActionQueue._undo_queue.append(action_item)
        
        if len(ActionQueue._redo_queue) < 0:
            print("Nothing to redo")
            return
        
        if action_item[1] == "add":
            ActionQueue._task_man_instance.add_task(action_item[0])
        
        elif action_item[1] == "delete":
            ActionQueue._task_man_instance.remove_task(action_item[0].task_id)
        
        elif action_item[1] == "edit":
            ActionQueue._undo_queue[-1][0] = ActionQueue._task_man_instance.tasks[action_item[0].task_id]
            ActionQueue._task_man_instance.tasks[action_item[0].task_id] = action_item[0]
        
        elif action_item[1] == "sort":
            ActionQueue._undo_queue[-1][0] = ActionQueue._task_man_instance.tasks
            ActionQueue._task_man_instance.tasks = action_item[0]
         