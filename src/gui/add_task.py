import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from ..cli.task import Task

class AddTaskHandler:
    """
    A handler for managing the Add Task functionality within the application.
    """
    def __init__(self, parent, task_manager, refresh_callback, calendar_view):
        self.parent = parent
        self.task_manager = task_manager
        self.refresh_callback = refresh_callback
        self.calendar_view = calendar_view
        self.create_widgets()

    def create_widgets(self):
        self.add_window = tk.Toplevel(self.parent)
        self.add_window.title("Add Task")
        self.add_window.geometry("300x575")
        self.add_window.grab_set()

        # Create all UI elements
        self._create_title_field()
        self._create_description_field()
        self._create_calendar()
        self._create_priority_menu()
        self._create_tags_field()
        self._create_action_buttons()

    def _create_title_field(self):
        tk.Label(self.add_window, text="Title:").pack(pady=5)
        self.title_entry = tk.Entry(self.add_window)
        self.title_entry.pack(pady=5)

    def _create_description_field(self):
        tk.Label(self.add_window, text="Description:").pack(pady=5)
        self.desc_entry = tk.Entry(self.add_window)
        self.desc_entry.pack(pady=5)

    def _create_calendar(self):
        tk.Label(self.add_window, text="Due Date:").pack(pady=5)
        self.calendar = Calendar(self.add_window, selectmode='day', date_pattern="yyyy-mm-dd")
        self.calendar.pack(pady=5)

    def _create_priority_menu(self):
        tk.Label(self.add_window, text="Priority:").pack(pady=5)
        self.priority_var = tk.StringVar(value="Medium")
        priority_menu = tk.OptionMenu(self.add_window, self.priority_var, "High", "Medium", "Low")
        priority_menu.pack(pady=5)

    def _create_tags_field(self):
        tk.Label(self.add_window, text="Tags (comma-separated):").pack(pady=5)
        self.tags_entry = tk.Entry(self.add_window)
        self.tags_entry.pack(pady=5)
        self._create_done_toggle()

    def _create_done_toggle(self):
        self.done_button = tk.Button(
            self.add_window, 
            text="Mark as Done", 
            command=self.toggle_done_tag
        )
        self.done_button.pack(pady=5)

    def _create_action_buttons(self):
        tk.Button(
            self.add_window, 
            text="Confirm", 
            command=self.confirm
        ).pack(pady=10)

    def toggle_done_tag(self):
        current_tags = self.tags_entry.get().split(",")
        current_tags = [tag.strip() for tag in current_tags if tag.strip()]
        
        if "Done" in current_tags:
            current_tags.remove("Done")
            self.done_button.config(text="Mark as Done")
        else:
            current_tags.append("Done")
            self.done_button.config(text="Unmark as Done")
            
        self.tags_entry.delete(0, tk.END)
        self.tags_entry.insert(0, ", ".join(current_tags))

    def confirm(self):
        title = self.title_entry.get().strip()
        description = self.desc_entry.get().strip()
        due_date = self.calendar.get_date()
        priority = self.priority_var.get()
        tags = [tag.strip() for tag in self.tags_entry.get().split(",") if tag.strip()]

        if not title:
            messagebox.showwarning("Input Error", "Title is required!")
            return

        new_task = Task(title, description, due_date, priority, tags)
        self.task_manager.add_task(new_task)
        self.refresh_callback()
        self.calendar_view.highlight_task_days()
        self.calendar_view.on_date_select(None)
        self.add_window.destroy()
