from abc import ABC, abstractmethod
from ..cli.task import Task as task
from ..cli.task_manager import TaskManager as task_manager

class Filterer(ABC):
    """Abstract base class for task filtering strategies"""
    @abstractmethod
    def filter(tasks: dict):
        pass
    
class PriorityFilterer(Filterer):
    """Strategy to filter by priority"""
    def filter(tasks: dict, priority: str) :
        for task in tasks.values():
            if task.priority == priority:
                task.visible = True
            else:
                task.visible = False

class TagFilterer(Filterer):
    """Strategy to filter by tags"""
    def filter(tasks: dict, tag: str):
        for task in tasks.values():
            if tag in task.tags:
                task.visible = True
            else:
                task.visible = False

class ShowAllFilterer(Filterer):
    """Strategy to filter nothing and show all tasks"""
    def filter(tasks: dict):
        for task in tasks.values():
            task.visible = True
    
class DefaultFilterer(Filterer):
    """Default filtering strategy"""
    def filter(tasks: dict):
        for task in tasks.values():
            task.visible = "Done" not in task.tags
            
class CompleteFilterer(Filterer):
    """Strategy to filter out tasks with the "Done" tag"""
    def filter(tasks: dict):
        for task in tasks.values():
            task.visible = "Done" in task.tags

