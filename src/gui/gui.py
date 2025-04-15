import sys
import tkinter as tk

from tkinter import ttk, messagebox, OptionMenu, Button, Label
from tkcalendar import Calendar

from .task_visualizer import TaskVisualizer
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from ..cli.task import Task
from ..cli.task_manager import TaskManager
from .sorter import Sorter, TitleSorter, DateSorter, PrioritySorter
from ..cli.taskstorage import TaskStorage
from .filterer import Filterer, PriorityFilterer, CompleteFilterer, ShowAllFilterer, DefaultFilterer, TagFilterer
from .calendar_view import CalendarView
from .colors import (
    BG_COLOR,
    SIDEBAR_COLOR,
    BUTTON_COLOR,
    BUTTON_HOVER,
    TEXT_COLOR,
    TASK_AREA_BG,
    TASK_TEXT_COLOR,
    HEADER_COLOR
)
from .treeview_style import configure_treeview_styles
from .add_task import AddTaskHandler
from .delete_task import DeleteTaskHandler
from .edit_task import EditTaskHandler
from .toggle_view import ToggleViewHandler


# Initialize App
root = tk.Tk()
root.title("Task Manager")
root.geometry("1000x650")
root.configure(bg=BG_COLOR)

# configures the treeview styles
configure_treeview_styles()

# Function to handle window close
def on_close():
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_close)

# Sidebar (Left Panel)
sidebar = tk.Frame(root, bg=SIDEBAR_COLOR, width=200)
sidebar.pack(side="left", fill="y")

# Task Manager instance
task_man = TaskManager()

# Button Hover Effects
def on_hover(event):
    event.widget.config(bg=BUTTON_HOVER)

def on_leave(event):
    event.widget.config(bg=BUTTON_COLOR)

# Main Task Area (Right Side) - Using grid layout
task_area = tk.Frame(root, bg=TASK_AREA_BG)
task_area.pack(side="right", expand=True, fill="both", padx=10, pady=10)

# Initialize the CalendarView
calendar_view = CalendarView(task_area, task_man, bg_color=BG_COLOR, text_color=TEXT_COLOR)

# Configure grid weights
task_area.rowconfigure(0, weight=1)  # Treeview will expand
task_area.rowconfigure(1, weight=0)  # Visualization has fixed height
task_area.columnconfigure(0, weight=1)

# Task Display (Treeview)
columns = ("Title", "Priority", "Due Date", "Description", "Tags")
task_tree = ttk.Treeview(task_area, columns=columns, show="headings", selectmode="browse", style="Treeview")

# Configure Treeview tags
task_tree.tag_configure("done", background="#D4EDDA", foreground="#155724")  # Green background for "Done" tasks
task_tree.tag_configure("default", background=TASK_AREA_BG, foreground=TASK_TEXT_COLOR)  # Default style

# Define column headings
for col in columns:
    task_tree.heading(col, text=col)
    task_tree.column(col, anchor="w", width=150)

# Add the Treeview to the task area (row 0)
task_tree.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Scrollbar for Treeview
scrollbar = ttk.Scrollbar(task_area, orient="vertical", command=task_tree.yview)
task_tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=4, sticky="ns")

# Visualization Panel (row 1)
viz_panel = tk.Frame(task_area, bg=TASK_AREA_BG, height=200)
viz_panel.grid(row=1, column=0, columnspan=5, sticky="nsew", pady=(10, 0))

# Initialize the visualizer
task_visualizer = TaskVisualizer(task_man)
viz_widget = None

def update_visualization():
    """Updates the visualization panel with current task data"""
    global viz_widget
    
    # Clear any existing visualization
    for widget in viz_panel.winfo_children():
        widget.destroy()
    
    # Create new visualization (either pie chart or "no tasks" message)
    viz_widget = task_visualizer.create_pie_chart(viz_panel)
    if viz_widget:  # Only pack if we got a widget back
        viz_widget.pack(fill="both", expand=True)

def display_tasks():
    """Updates both the task list and visualization"""
    task_tree.delete(*task_tree.get_children())  # Clear existing data

    for task_id, task in task_man.tasks.items():
        tags_str = ", ".join(sorted(task.tags)) if task.tags else ""
        row_tag = "done" if "Done" in task.tags else "default"
        task_tree.insert("", "end", iid=task_id, values=(task.title, task.priority, task.due_date, task.description, tags_str), tags=(row_tag))
    
    update_visualization()

# Implements the add button and all of its logic from AddTaskDialog Class
def add_button():
    AddTaskHandler(root, task_man, display_tasks, calendar_view)

# Implements the delete button and all the logic from DeleteTaskHandler
def delete_button():
    DeleteTaskHandler(task_tree, task_man, display_tasks, calendar_view).execute()

# Implemetns the edit button and all the logic from EditTaskHandler
def edit_button():
    EditTaskHandler(root, task_tree, task_man, display_tasks, calendar_view)

# Implements the toggle view button and all the logic from ToggleViewHandler
def toggle_view():
    ToggleViewHandler(task_tree, calendar_view).toggle()
    
# Save/Load Functions
def save_button():
    storage_handler = TaskStorage()
    storage_handler.save_tasks(task_man.tasks)

def load_button():
    storage_handler = TaskStorage()
    storage_handler.load_tasks(task_man)
    display_tasks()

# Sort Function
def sort_button():
    sort_window = tk.Toplevel(root)
    sort_window.title("Sort By")
    sort_window.geometry("300x400")
    
    sort_options = ["Title", "Date", "Priority"]
    
    user_option = tk.StringVar()
    user_option.set(sort_options[0])
    
    dropdown = OptionMenu(sort_window, user_option, *sort_options)
    dropdown.pack()
    
    
    def press_sort():
        print(task_man.tasks)
        option = user_option.get()
        sorter = Sorter()
        if option == sort_options[0]:
            sorter = TitleSorter()
        elif option == sort_options[1]:
            sorter = DateSorter()
        elif option == sort_options[2]:
            sorter = PrioritySorter()
        task_man.tasks = sorter.sort_tasks(task_man.tasks)
        display_tasks()
        sort_window.destroy()
        return
        
    sub_button = Button(sort_window, text = "Sort", command = press_sort)
    sub_button.pack(padx=20, pady=20)
    

# Sidebar Buttons
buttons = [
    ("Add Task", add_button), 
    ("Edit Task", edit_button),
    ("Delete Task", delete_button), 
    ("Save Tasks", save_button), 
    ("Load Tasks", load_button),
    ("Sort Tasks", sort_button),
    #("Filter Tasks", filter_button)
    ("Toggle View", toggle_view)
]

for btn_text, command in buttons:
    btn = tk.Button(sidebar, text=btn_text, bg=BUTTON_COLOR, fg=TEXT_COLOR, bd=0, relief="flat", height=2, command=command)
    btn.pack(fill="x", padx=15, pady=25)
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)

# Initial display
display_tasks()

# Run App
root.mainloop()


# Run App
root.mainloop()

