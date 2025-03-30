import task, task_manager
from abc import ABC, abstractmethod

class Sorter:
    @abstractmethod
    def sort_tasks(self, input_dict: dict) -> dict:
        pass

class TitleSorter(Sorter):
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
                if task.title == title_to_match:
                    sorted_dict[keys[task_iter]] = values[task_iter]
                    continue
                else:
                    task_iter += 1
            dict_counter += 1  
                
        return sorted_dict
    
class DateSorter(Sorter):
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
            title_to_match = list_of_dates[dict_counter]
            for task in input_dict.items():
                if task.title == title_to_match:
                    sorted_dict[keys[task_iter]] = values[task_iter]
                    continue
                else:
                    task_iter += 1
            dict_counter += 1  
                
        return sorted_dict
    
class PrioritySorter(Sorter):
    def sort_tasks(self, input_dict: dict, descending: bool = False) -> dict:
        list_of_priorities = []
        for task_item in input_dict.values():
            list_of_priorities.append(task_item.priority)
        list_of_priorities.sort(reverse=descending)
        sorted_dict = {}
        dict_counter = 0
        keys = list(input_dict.keys())
        values = list(input_dict.values())
        while dict_counter < len(list_of_priorities):
            task_iter = 0
            title_to_match = list_of_priorities[dict_counter]
            for task in input_dict.items():
                if task.title == title_to_match:
                    sorted_dict[keys[task_iter]] = values[task_iter]
                    continue
                else:
                    task_iter += 1
            dict_counter += 1  
                
        return sorted_dict
    
class TagSorter(Sorter):
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
                if task.title == title_to_match:
                    sorted_dict[keys[task_iter]] = values[task_iter]
                    continue
                else:
                    task_iter += 1
            dict_counter += 1  
                
        return sorted_dict