import tkinter as tk

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
root.geometry("800x500")
root.configure(bg=BG_COLOR)

# Sidebar (Left Panel)
sidebar = tk.Frame(root, bg=SIDEBAR_COLOR, width=200)
sidebar.pack(side="left", fill="y")

# Task Area (Right Side)
task_area = tk.Frame(root, bg=TASK_AREA_BG)
task_area.pack(side="right", expand=True, fill="both", padx=10, pady=10)

# Buttons in Sidebar
def on_hover(event):
    event.widget.config(bg=BUTTON_HOVER)

def on_leave(event):
    event.widget.config(bg=BUTTON_COLOR)

buttons = ["Add Task", "Delete Task", "Save Task", "Load Task"]
for btn_text in buttons:
    btn = tk.Button(sidebar, text=btn_text, bg=BUTTON_COLOR, fg=TEXT_COLOR, bd=0, relief="flat", height=2)
    btn.pack(fill="x", padx=15, pady=25)
    
    # Bind hover effects
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)

# Task Grid Area
header_labels = ["Name", "Priority", "Date", "Description"]  # Reordered
for col, text in enumerate(header_labels):
    header = tk.Label(task_area, text=text, bg=HEADER_COLOR, fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
    header.grid(row=0, column=col, sticky="ew", padx=2, pady=2)

# Sample Task Data (Reordered to match headers)
tasks = [
    ("Project A", "High", "2025-02-26", "Finish the report"),
    ("Meeting", "Medium", "2025-03-01", "Team sync-up"),
    ("Review", "Low", "2025-03-05", "Code review for feature X")
]

# Display tasks in the grid
for row, task in enumerate(tasks, start=1):
    for col, value in enumerate(task):
        cell = tk.Label(task_area, text=value, bg="white", fg=TASK_TEXT_COLOR, font=("Arial", 10), padx=10, pady=5)
        cell.grid(row=row, column=col, sticky="ew", padx=2, pady=2)

# Ensure columns expand equally
for col in range(4):
    task_area.columnconfigure(col, weight=1)

# Run the app
root.mainloop()
