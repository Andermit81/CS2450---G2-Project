from src.sorter import Sorter, TitleSorter, DateSorter, PrioritySorter

from src.task_manager import TaskManager

from src.task import Task

title_sorter = TitleSorter()
date_sorter = DateSorter()
priority_sorter = PrioritySorter()

new_taskman = TaskManager()

task1 = Task("a", "desc", "20000101", "Medium")
task2 = Task("b", "desc", "19990101", "Low")
task3 = Task("c", "desc", "20010101", "High")

new_taskman.add_task(task3)
new_taskman.add_task(task2)
new_taskman.add_task(task1)

assert new_taskman.tasks == {task3.task_id: task3, task2.task_id: task2, task1.task_id: task1}
task_dict = new_taskman.tasks
assert title_sorter.sort_tasks(task_dict) == {task1.task_id: task1, task2.task_id: task2, task3.task_id: task3}
assert date_sorter.sort_tasks(task_dict) == {task2.task_id: task2, task1.task_id: task1, task3.task_id: task3}
assert priority_sorter.sort_tasks(task_dict) == {task3.task_id: task3, task1.task_id: task1, task2.task_id: task2}


