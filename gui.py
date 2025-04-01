import sys
import tkinter as tk

from tkinter import ttk, messagebox, OptionMenu, Button, Label

from task_visualizer import TaskVisualizer
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from task import Task
from task_manager import TaskManager
from sorter import Sorter, TitleSorter, DateSorter, PrioritySorter
from taskstorage import TaskStorage

# Colors
BG_COLOR = "#F5F7FA"  # Main background
SIDEBAR_COLOR = "#2C3E50"  # Sidebar background
BUTTON_COLOR = "#34495E"  # Button color
BUTTON_HOVER = "#1ABC9C"  # Button hover
TEXT_COLOR = "black"  # Sidebar text
TASK_AREA_BG = "#ECF0F1"  # Task area background
TASK_TEXT_COLOR = "#333333"  # Task text
HEADER_COLOR = "#1ABC9C"  # Table header color

# Initialize App
root = tk.Tk()
root.title("Task Manager")
root.geometry("1000x600")
root.configure(bg=BG_COLOR)

# Function to handle window close
def on_close():
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_close)

# Treeview Styling
style = ttk.Style()
style.theme_use("default")  # Use the default theme as a base

# Configure Treeview style
style.configure("Treeview",
                background=TASK_AREA_BG,
                foreground=TASK_TEXT_COLOR,
                fieldbackground=BG_COLOR,
                rowheight=25,
                font=('Arial', 15))

style.configure("Treeview.Heading",
                background=HEADER_COLOR,
                foreground="black",
                font=('Arial', 15, 'bold'))

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

# Function to Add Task
def add_button():
    add_window = tk.Toplevel(root)
    add_window.title("Add Task")
    add_window.geometry("300x450")

    add_window.grab_set()

    tk.Label(add_window, text="Title:").pack(pady=5)
    title_entry = tk.Entry(add_window)
    title_entry.pack(pady=5)

    tk.Label(add_window, text="Description:").pack(pady=5)
    desc_entry = tk.Entry(add_window)
    desc_entry.pack(pady=5)

    #Validation for Due Date
    def validate_date_date_input(new_value):
        return all(char.isdigit() or char == "-" for char in new_value) and len(new_value) <= 10
    
    vcmd = (root.register(validate_date_date_input), '%P')

    tk.Label(add_window, text="Due Date (YYYY-MM-DD):").pack(pady=5)
    due_date_entry = tk.Entry(add_window, validate="key", validatecommand=vcmd)
    due_date_entry.pack(pady=5)

    tk.Label(add_window, text="Priority:").pack(pady=5)
    priority_var = tk.StringVar(value="Medium")
    priority_menu = tk.OptionMenu(add_window, priority_var, "High", "Medium", "Low")
    priority_menu.pack(pady=5)

    tk.Label(add_window, text="Tags (comma-separated):").pack(pady=5)
    tags_entry = tk.Entry(add_window)
    tags_entry.pack(pady=5)

    def add_done_tag():
        current_tags = tags_entry.get().split(",")
        current_tags = [tag.strip() for tag in current_tags if tag.strip()]  # Clean up whitespace
        if "Done" in current_tags:
            current_tags.remove("Done")  # Remove "Done" if it exists
        else:
            current_tags.append("Done")  # Add "Done" if it doesn't exist
        updated_tags = ", ".join(current_tags)
        tags_entry.delete(0, tk.END)
        tags_entry.insert(0, updated_tags)

    def confirm():
        title = title_entry.get()
        description = desc_entry.get()
        due_date = due_date_entry.get()
        priority = priority_var.get()
        tags_input = tags_entry.get()
        tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []

        if not title.strip():
            messagebox.showwarning("Input Error", "Title is required!")
            return
        
        new_task = Task(title, description, due_date, priority, tags)
        task_man.add_task(new_task)
        display_tasks()
        add_window.destroy()
    
    tk.Button(add_window, text="Mark as Done", command=add_done_tag).pack(pady=5)
    tk.Button(add_window, text="Confirm", command=confirm).pack(pady=10)

# Function to Delete Task
def delete_button():
    selected_item = task_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a task to delete!")
        return

    confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this task?")
    if not confirm:
        return
    
    for item in selected_item:
        task_id = item
        if task_id in task_man.tasks:
            task_man.remove_task(task_id)
        task_tree.delete(item)
    display_tasks()  # Update visualization after deletion

# Function to edit task
def edit_button():
    selected_item = task_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a task to edit!")
        return
        
    task_id = selected_item[0]
    task = task_man.tasks.get(task_id)

    if not task:
        messagebox.showerror("Error", "Task not found!")
        return
        
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Task")
    edit_window.geometry("300x450")

    edit_window.grab_set()

    tk.Label(edit_window, text="Title:").pack(pady=5)
    title_entry = tk.Entry(edit_window)
    title_entry.insert(0, task.title)
    title_entry.pack(pady=5)

    tk.Label(edit_window, text="Description:").pack(pady=5)
    desc_entry = tk.Entry(edit_window)
    desc_entry.insert(0, task.description)
    desc_entry.pack(pady=5)

    # Validation for Due Date
    def validate_date_input(new_value):
        return all(char.isdigit() or char == "-" for char in new_value) and len(new_value) <= 10
    
    vcmd = (root.register(validate_date_input), '%P')

    tk.Label(edit_window, text="Due Date (YYYY-MM-DD):").pack(pady=5)
    due_date_entry = tk.Entry(edit_window, validate="key", validatecommand=vcmd)
    due_date_entry.insert(0, task.due_date if task.due_date else "")
    due_date_entry.pack(pady=5)

    tk.Label(edit_window, text="Priority:").pack(pady=5)
    priority_var = tk.StringVar(value=task.priority)
    priority_menu = tk.OptionMenu(edit_window, priority_var, "High", "Medium", "Low")
    priority_menu.pack(pady=5)

    tk.Label(edit_window, text="Tags (comma-separated):").pack(pady=5)
    tags_entry = tk.Entry(edit_window)
    tags_entry.insert(0, ", ".join(task.tags) if task.tags else "")
    tags_entry.pack(pady=5)

    def toggle_done_tag():
        current_tags = tags_entry.get().split(",")
        current_tags = [tag.strip() for tag in current_tags if tag.strip()]  # Clean up whitespace
        if "Done" in current_tags:
            current_tags.remove("Done")  # Remove "Done" if it exists
        else:
            current_tags.append("Done")  # Add "Done" if it doesn't exist
        updated_tags = ", ".join(current_tags)
        tags_entry.delete(0, tk.END)
        tags_entry.insert(0, updated_tags)

        display_tasks()

    def confirm_edit():
        new_title = title_entry.get().strip()
        new_description = desc_entry.get().strip()
        new_due_date = due_date_entry.get().strip()
        new_priority= priority_var.get().strip()
        new_tags_input = tags_entry.get().strip()

        if new_title:
            task.title = new_title
        if new_description:
            task.description = new_description
        if new_due_date:
            task.due_date = new_due_date
        if new_priority in ["High", "Medium", "Low"]:
            task.priority = new_priority
        
        task.tags = [tag.strip() for tag in new_tags_input.split(",")] if new_tags_input else []

        display_tasks()
        edit_window.destroy()
        messagebox.showinfo("Success", "Task updated successfully!")

    tk.Button(edit_window, text="Mark as Done", command=toggle_done_tag).pack(pady=5)
    tk.Button(edit_window, text="Save Changes", command=confirm_edit).pack(pady=10)

# Save/Load Functions
def save_button():
    storage_handler = TaskStorage()
    storage_handler.save_tasks(task_man.tasks)

def load_button():
    storage_handler = TaskStorage()
    storage_handler.load_tasks(task_man)
    display_tasks()
    
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
    ("Sort Tasks", sort_button)
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

