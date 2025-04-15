import tkinter as tk
from tkinter import messagebox
from ..cli.task import Task

class DeleteTaskHandler:
    def __init__(self, task_tree, task_manager, refresh_callback, calendar_view):
        """
        Class for deleting existing tasks
        
        Parameters:
        - task_tree: Reference to the Treeview widget
        - task_manager: TaskManager instance
        - refresh_callback: Function to update the display
        """
        self.task_tree = task_tree
        self.task_manager = task_manager
        self.refresh_callback = refresh_callback
        self.calendar_view = calendar_view

    def execute(self):
        """Main entry point for deletion process"""
        selected_items = self._get_selected_items()
        if not selected_items:
            selected_task_id = self.calendar_view.get_selected_task_id()
            if selected_task_id:
                selected_items = [selected_task_id]
            else:
                return

        if self._confirm_deletion():
            self._perform_deletion(selected_items)
            self.refresh_callback()
            self.calendar_view.highlight_task_days()
            self.calendar_view.on_date_select(None)

    def _get_selected_items(self):
        """Returns list of selected item IDs or shows warning"""
        selected = self.task_tree.selection()
        if not selected:
            # Check CalendarView's Listbox selection
            selected_task_id = self.calendar_view.get_selected_task_id()
            if selected_task_id:
                return [selected_task_id]  # Return the selected task ID as a list
            else:
                messagebox.showwarning("Warning", "Please select a task to delete!")
                return None
        return selected

    def _confirm_deletion(self):
        """Shows confirmation dialog"""
        return messagebox.askyesno(
            "Confirm Deletion", 
            "Are you sure you want to delete the selected task(s)?"
        )

    def _perform_deletion(self, items):
        """Actually removes tasks from manager and treeview"""
        for item_id in items:
            if item_id in self.task_manager.tasks:
                self.task_manager.remove_task(item_id)
            self.task_tree.delete(item_id)
