import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

class EditTaskHandler:
    def __init__(self, parent, task_tree, task_manager, refresh_callback, calendar_view, task_id = None):
        """
        Parameters:
        - parent: Main application window (tk.Tk)
        - task_tree: Treeview widget reference
        - task_manager: TaskManager instance
        - refresh_callback: Function to refresh the task display
        """
        self.parent = parent
        self.task_tree = task_tree
        self.task_manager = task_manager
        self.refresh_callback = refresh_callback
        self.calendar_view = calendar_view
        self.task_id = task_id 
        self.task = None # Will hold the selected task
        
        # Validate selection and initialize
        if task_id:
            self.task = self.task_manager.tasks.get(task_id)
        else:
            selected_item = self._validate_selection()
            if not selected_item:
                # Try to get the selected task from the CalendarView
                selected_item = self.calendar_view.get_selected_task_id()
            if selected_item:
                self.task = self.task_manager.tasks.get(selected_item)

        if self.task:
            self._create_dialog()
        else:
            messagebox.showerror("Error", "Task not found!")

    def _validate_selection(self):
        """Ensure a task is selected in the Treeview"""
        selected = self.task_tree.selection()
        if not selected:
            selected_task_id = self.calendar_view.get_selected_task_id()
            if selected_task_id:
                return selected_task_id
            else:
                messagebox.showwarning("Warning", "Please select a task to edit!")
                return None
        return selected[0]

    def _create_dialog(self):
        """Create the edit task dialog window"""
        self.edit_window = tk.Toplevel(self.parent)
        self.edit_window.title("Edit Task")
        self.edit_window.geometry("300x575")
        self.edit_window.grab_set()

        # Create widgets
        self._create_title_field()
        self._create_description_field()
        self._create_calendar()
        self._create_priority_menu()
        self._create_tags_field()
        self._create_action_buttons()

    def _create_title_field(self):
        tk.Label(self.edit_window, text="Title:").pack(pady=5)
        self.title_entry = tk.Entry(self.edit_window)
        self.title_entry.insert(0, self.task.title)
        self.title_entry.pack(pady=5)

    def _create_description_field(self):
        tk.Label(self.edit_window, text="Description:").pack(pady=5)
        self.desc_entry = tk.Entry(self.edit_window)
        self.desc_entry.insert(0, self.task.description)
        self.desc_entry.pack(pady=5)

    def _create_calendar(self):
        tk.Label(self.edit_window, text="Due Date:").pack(pady=5)
        self.calendar = Calendar(
            self.edit_window, 
            selectmode='day', 
            date_pattern="yyyy-mm-dd"
        )
        # Safely set date if available
        if self.task.due_date:
            try:
                self.calendar.selection_set(self.task.due_date)
            except Exception:
                print("Fallback to today's date")  # Fallback to today's date
        self.calendar.pack(pady=5)

    def _create_priority_menu(self):
        tk.Label(self.edit_window, text="Priority:").pack(pady=5)
        self.priority_var = tk.StringVar(value=self.task.priority)
        tk.OptionMenu(
            self.edit_window, 
            self.priority_var, 
            "High", 
            "Medium", 
            "Low"
        ).pack(pady=5)

    def _create_tags_field(self):
        tk.Label(self.edit_window, text="Tags (comma-separated):").pack(pady=5)
        self.tags_entry = tk.Entry(self.edit_window)
        self.tags_entry.insert(0, ", ".join(self.task.tags) if self.task.tags else "")
        self.tags_entry.pack(pady=5)
        self._create_done_toggle()

    def _create_done_toggle(self):
        initial_text = "Unmark as Done" if "Done" in self.task.tags else "Mark as Done"
        self.done_button = tk.Button(
            self.edit_window,
            text=initial_text,
            command=self._toggle_done_tag
        )
        self.done_button.pack(pady=5)

    def _create_action_buttons(self):
        tk.Button(
            self.edit_window,
            text="Save Changes",
            command=self._save_changes
        ).pack(pady=10)

    def _toggle_done_tag(self):
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

    def _save_changes(self):
        """Handle saving edited task details"""
        # Get updated values
        new_title = self.title_entry.get().strip()
        new_description = self.desc_entry.get().strip()
        new_due_date = self.calendar.get_date().strip()
        new_priority = self.priority_var.get().strip()
        new_tags = [t.strip() for t in self.tags_entry.get().split(",") if t.strip()]

        try:
            datetime.strptime(new_due_date, "%Y-%m-%d")  # Ensure valid date format
        except ValueError:
            messagebox.showerror("Error", "Invalid due date format. Please select a valid date.")
            return

        # Update task properties
        if new_title:
            self.task.title = new_title
        self.task.description = new_description  # Allow empty
        self.task.due_date = new_due_date
        self.task.priority = new_priority
        self.task.tags = new_tags

        # Refresh UI and close
        self.refresh_callback()
        self.calendar_view.highlight_task_days()
        self.calendar_view.on_date_select(None)
        messagebox.showinfo("Success", "Task updated successfully!")
        self.edit_window.destroy()
