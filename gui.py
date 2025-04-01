import tkinter as tk
from tkinter import ttk, messagebox, OptionMenu, Button, Label
from task import Task
from task_manager import TaskManager
from sorter import Sorter, TagSorter, TitleSorter, DateSorter, PrioritySorter

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
root.geometry("1000x500")
root.configure(bg=BG_COLOR)

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

# Task Area (Right Side)
task_area = tk.Frame(root, bg=TASK_AREA_BG)
task_area.pack(side="right", expand=True, fill="both", padx=10, pady=10)

# Task Display (Treeview)
columns = ("Title", "Priority", "Due Date", "Description", "Tags")
task_tree = ttk.Treeview(task_area, columns=columns, show="headings", selectmode="browse", style="Treeview")

# Define column headings
for col in columns:
    task_tree.heading(col, text=col)
    task_tree.column(col, anchor="w", width=150)

# Add the Treeview to the task area
task_tree.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Scrollbar for Treeview
scrollbar = ttk.Scrollbar(task_area, orient="vertical", command=task_tree.yview)
task_tree.configure(yscrollcommand=scrollbar.set)  # Bind the scrollbar to the Treeview
scrollbar.grid(row=1, column=4, sticky="ns")

# Ensure columns expand equally
task_area.columnconfigure(0, weight=1)
task_area.columnconfigure(1, weight=1)
task_area.columnconfigure(2, weight=1)
task_area.columnconfigure(3, weight=1)

# Function to Display Tasks in Treeview
def display_tasks():
    task_tree.delete(*task_tree.get_children())  # Clear existing data

    for task_id, task in task_man.tasks.items():
        tags_str = ", ".join(sorted(task.tags)) if task.tags else "No tags"
        task_tree.insert("", "end", iid=task_id, values=(task.title, task.priority, task.due_date, task.description, tags_str))

# Function to Add Task
def add_button():
    add_window = tk.Toplevel(root)
    add_window.title("Add Task")
    add_window.geometry("300x400")

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

    tk.Label(add_window, text="Tags (comma-separated):").pack(pady=5)
    tags_entry = tk.Entry(add_window)
    tags_entry.pack(pady=5)

    def add_done_tag():
        current_tags = tags_entry.get()
        if "Done" not in current_tags.split(","):
            updated_tags = f"{current_tags}, Done" if current_tags else "Done"
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

#Function to edit task
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
    edit_window.geometry("300x400")

    tk.Label(edit_window, text="Title:").pack(pady=5)
    title_entry = tk.Entry(edit_window)
    title_entry.insert(0, task.title) #Pre-fill with existing data
    title_entry.pack(pady=5)

    tk.Label(edit_window, text="Description:").pack(pady=5)
    desc_entry = tk.Entry(edit_window)
    desc_entry.insert(0, task.description)
    desc_entry.pack(pady=5)

    tk.Label(edit_window, text="Due Date (YYYY-MM-DD):").pack(pady=5)
    due_date_entry = tk.Entry(edit_window)
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
        if "Done" in current_tags:
            current_tags.remove("Done")
        else:
            current_tags.append("Done")
        updated_tags = ", ".join(tag.strip() for tag in current_tags if tag.strip())
        tags_entry.delete(0, tk.END)
        tags_entry.insert(0, updated_tags)

    def confirm_edit():
        new_title = title_entry.get().strip()
        new_description = desc_entry.get().strip()
        new_due_date = due_date_entry.get().strip()
        new_priority= priority_var.get().strip()
        new_tags_input = tags_entry.get().strip()

        # Update task fields
        if new_title:
            task.title = new_title
        if new_description:
            task.description = new_description
        if new_due_date:
            task.due_date = new_due_date
        if new_priority in ["High", "Medium", "Low"]:
            task.priority = new_priority
        if new_tags_input:
            task.tags = [tag.strip() for tag in new_tags_input.split(",")]

        display_tasks()
        edit_window.destroy()
        messagebox.showinfo("Success", "Task updated successfully!")

    tk.Button(edit_window, text="Mark as Done", command=toggle_done_tag).pack(pady=5)
    tk.Button(edit_window, text="Save Changes", command=confirm_edit).pack(pady=10)

# Placeholder Save/Load Functions
def save_button():
    print("Saving tasks...")
    task_man.save_tasks()
    print("Tasks saved!")

def load_button():
    print("Loading tasks...")
    task_man.load_tasks()
    display_tasks()
    print("Tasks loaded!")
    
def sort_button():
    sort_window = tk.Toplevel(root)
    sort_window.title("Sort By")
    sort_window.geometry("300x400")
    
    sort_options = ["Title", "Date", "Priority", "Tag"]
    
    user_option = tk.StringVar()
    user_option.set(sort_options[0])
    
    dropdown = OptionMenu(sort_window, user_option, *sort_options)
    dropdown.pack()
    
    
    def press_sort(option=user_option.get()):
        sorter = Sorter()
        if option == sort_options[0]:
            sorter = TitleSorter()
        elif option == sort_options[1]:
            sorter == DateSorter()
        elif option == sort_options[2]:
            sorter == PrioritySorter()
        else:
            sorter == TagSorter()
        task_man.tasks = sorter.sort_tasks(task_man.tasks)
        print(task_man.tasks)
        task_man.view_tasks()
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
    
    # Bind hover effects
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)

# Run App
root.mainloop()

