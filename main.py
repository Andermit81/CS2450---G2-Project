import json
from task import Task
from task_manager import TaskManager

def main():
    task_man = TaskManager()
    running = True
    print("Welcome to the task manager! Please select an option: ")
    while running:
        print("Option 1: Add Task")
        print("Option 2: Remove Task")
        print("Option 3: View Tasks")
        print("Option 4: Save Tasks")
        print("Option 5: Load Tasks")
        print("Default Option: Quit Task Manager")
        option = input("Select a number, or press anything else to quit: ")
        match option:
            case "1":
                task_name = input("What's the task name? ")
                task_desc = input("Enter a description, or press 'enter' without a description to leave blank: ")
                task_due_date = input("Enter a due date, or press 'enter' without a due date to leave blank: ")
                task_priority = input("If you wish to edit the priority, enter 'high' or 'low', or leave blank for 'medium': ")
                if task_due_date == "":
                    task_due_date = None
                if task_priority.lower in ["low", "high"]:
                    task_priority = task_priority.capitalize()
                    
                task_man.add_task(task_name, task_desc, task_due_date, task_priority)
                break
            case "2":
                task_id = input("Enter the ID of the task you wish to remove: ")
                task_man.remove_task(task_id)
                break
            case "3":
                task_man.view_tasks()
                break
            case "4":
                task_man.save_tasks()
                break
            case "5":
                task_man.load_tasks()
                break
            case _:
                running = False
                print("Thank you for using Task Manager!")
if __name__ == "__main__":
    main()