from abc import ABC, abstractmethod
import task, task_manager

class Filterer(ABC):
    @abstractmethod
    def filter(tasks: dict):
        pass
    
class PriorityFilterer(Filterer):
    def filter(tasks: dict, priority: str) :
        for task in tasks.values():
            if task.priority == priority:
                task.visible = True
            else:
                task.visible = False

class TagFilterer(Filterer):
    def filter(tasks: dict, tag: str):
        for task in tasks.values():
            if tag in task.tags:
                task.visible = True
            else:
                task.visible = False

class ShowAllFilterer(Filterer):
    def filter(tasks: dict):
        for task in tasks.values():
            task.visible = True
    
class DefaultFilter(Filterer):
    def filter(tasks: dict):
        for task in tasks.values():
            task.visible = "Done" not in task.tags

