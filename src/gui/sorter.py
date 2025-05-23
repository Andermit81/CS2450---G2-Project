from ..cli.task import Task as task
from ..cli.task_manager import TaskManager as task_manager
from abc import ABC, abstractmethod

class Sorter:
    """Abstract base class for task sorting strategies"""
    @abstractmethod
    def sort_tasks(self, input_dict: dict) -> dict:
        pass

class TitleSorter(Sorter):
    """strategy to sort the tasks by title"""
    def sort_tasks(self, input_dict: dict, descending: bool = False) -> dict:
        list_of_titles = []
        for task_item in input_dict.values():
            list_of_titles.append(task_item.title)
        list_of_titles.sort(reverse=descending)
        sorted_dict = {}
        dict_counter = 0
        keys = list(input_dict.keys())
        values = list(input_dict.values())
        while dict_counter < len(list_of_titles):
            task_iter = 0
            title_to_match = list_of_titles[dict_counter]
            for task in input_dict.items():
                if task[1].title == title_to_match:
                    sorted_dict[keys[task_iter]] = values[task_iter]
                    continue
                else:
                    task_iter += 1
            dict_counter += 1  
                
        return sorted_dict
    
class DateSorter(Sorter):
    """Strategy to sort the tasks by date"""
    def sort_tasks(self, input_dict: dict, descending: bool = False) -> dict:
        list_of_dates = []
        for task_item in input_dict.values():
            list_of_dates.append(task_item.due_date)
        list_of_dates.sort(reverse=descending)
        sorted_dict = {}
        dict_counter = 0
        keys = list(input_dict.keys())
        values = list(input_dict.values())
        while dict_counter < len(list_of_dates):
            task_iter = 0
            date_to_match = list_of_dates[dict_counter]
            for task in input_dict.items():
                if task[1].due_date == date_to_match:
                    sorted_dict[keys[task_iter]] = values[task_iter]
                    continue
                else:
                    task_iter += 1
            dict_counter += 1  
                
        return sorted_dict
    
class PrioritySorter(Sorter):
    """Strategy to sort tasks by their priority rating"""
    def priority_sort(self, priority):
        criteria = ["High", "Medium", "Low"]
        return criteria.index(priority)
    
    def sort_tasks(self, input_dict: dict, descending: bool = False) -> dict:
        list_of_priorities = []
        for task_item in input_dict.values():
            list_of_priorities.append(task_item.priority)
        list_of_priorities.sort(reverse=descending, key=self.priority_sort)
        sorted_dict = {}
        dict_counter = 0
        keys = list(input_dict.keys())
        values = list(input_dict.values())
        while dict_counter < len(list_of_priorities):
            task_iter = 0
            priority_to_match = list_of_priorities[dict_counter]
            for task in input_dict.items():
                if task[1].priority == priority_to_match and task[1] not in sorted_dict.values():
                    sorted_dict[keys[task_iter]] = values[task_iter]
                    continue
                else:
                    task_iter += 1
            dict_counter += 1  
                
        return sorted_dict
    
class TagSorter(Sorter):
    """Strategy to sort tasks based on their tags"""
    def sort_tasks(self, input_dict: dict, descending: bool = False) -> dict:
        list_of_titles = []
        for task_item in input_dict.values():
            list_of_titles.append(task_item.title)
        list_of_titles.sort(reverse=descending)
        sorted_dict = {}
        dict_counter = 0
        keys = list(input_dict.keys())
        values = list(input_dict.values())
        print(len(list_of_titles))
        while dict_counter < len(list_of_titles):
            print("New while loop")
            task_iter = 0
            title_to_match = list_of_titles[dict_counter]
            for task in input_dict.items():
                if task.title == title_to_match:
                    sorted_dict[keys[task_iter]] = values[task_iter]
                    continue
                else:
                    task_iter += 1
            dict_counter += 1  
                
        return sorted_dict
