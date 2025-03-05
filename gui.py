import tkinter as tk
from tkinter import ttk, messagebox
from task import Task
from task_manager import TaskManager

# Colors
BG_COLOR = "#F5F7FA"  
SIDEBAR_COLOR = "#2C3E50"  
BUTTON_COLOR = "#34495E"  
BUTTON_HOVER = "#1ABC9C"  
TEXT_COLOR = "black"  
TASK_AREA_BG = "#ECF0F1"  
HEADER_COLOR = "#1ABC9C" 

# Initialize App
root = tk.Tk()
root.title("Task Manager")
root.geometry("800x500")
root.configure(bg=BG_COLOR)

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
    

# Task Display (Treeview)
task_frame = tk.Frame(root, bg=TASK_AREA_BG)
task_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

# Create Treeview
columns = ("Title", "Priority", "Due Date", "Description")
task_tree = ttk.Treeview(task_frame, columns=columns, show="headings", selectmode="browse", style="Treeview")

# Define column headings
for col in columns:
    task_tree.heading(col, text=col)
    task_tree.column(col, anchor="w", width=150)

# Add the Treeview to the task area
task_tree.pack(expand=True, fill="both")

# Scrollbar for Treeview
scrollbar = ttk.Scrollbar(task_frame, orient="vertical", command=task_tree.yview)
task_tree.configure(yscrollcommand=scrollbar.set)  # Bind the scrollbar to the Treeview

# Use `grid` layout for the task_frame to control the layout better
task_tree.grid(row=0, column=0, sticky="nsew")  # Treeview in grid, expand to fill space
scrollbar.grid(row=0, column=1, sticky="ns")  # Scrollbar in grid, align to the right

# Ensure the grid expands properly with the content
task_frame.grid_rowconfigure(0, weight=1)
task_frame.grid_columnconfigure(0, weight=1)

# Function to Display Tasks in Treeview
def display_tasks():
    task_tree.delete(*task_tree.get_children())  # Clear existing data

    for task_id, task in task_man.tasks.items():
        task_tree.insert("", "end", iid=task_id, values=(task.title, task.priority, task.due_date, task.description))


# Function to Add Task
def add_button():
    add_window = tk.Toplevel(root)
    add_window.title("Add Task")
    add_window.geometry("300x350")

    tk.Label(add_window, text="Title:").pack(pady=5)
    title_entry = tk.Entry(add_window)
    title_entry.pack(pady=5)

    tk.Label(add_window, text="Description:").pack(pady=5)
    desc_entry = tk.Entry(add_window)
    desc_entry.pack(pady=5)

    tk.Label(add_window, text="Due Date (YYYY-MM-DD):").pack(pady=5)
    due_date_entry = tk.Entry(add_window)
    due_date_entry.pack(pady=5)

    tk.Label(add_window, text="Priority:").pack(pady=5)
    priority_var = tk.StringVar(value="Medium")
    priority_menu = tk.OptionMenu(add_window, priority_var, "High", "Medium", "Low")
    priority_menu.pack(pady=5)

    def confirm():
        title = title_entry.get()
        description = desc_entry.get()
        due_date = due_date_entry.get()
        priority = priority_var.get()

        if not title.strip():
            messagebox.showwarning("Input Error", "Title is required!")
            return
        
        new_task = Task(title, description, due_date, priority)
        task_man.add_task(new_task)
        display_tasks()
        add_window.destroy()
    
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


# Placeholder Save/Load Functions
def save_button():
    print("Saving tasks...")

def load_button():
    print("Loading tasks...")

# Sidebar Buttons
buttons = [
    ("Add Task", add_button), 
    ("Delete Task", delete_button), 
    ("Save Tasks", save_button), 
    ("Load Tasks", load_button)
]

for btn_text, command in buttons:
    btn = tk.Button(sidebar, text=btn_text, bg=BUTTON_COLOR, fg=TEXT_COLOR, bd=0, relief="flat", height=2, command=command)
    btn.pack(fill="x", padx=15, pady=25)
    
    # Bind hover effects
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)

# Run App
root.mainloop()
