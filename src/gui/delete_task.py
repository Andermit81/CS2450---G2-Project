import tkinter as tk
from tkinter import messagebox
from ..cli.task import Task

class DeleteTaskHandler:
    def __init__(self, task_tree, task_manager, refresh_callback):
        """
        Parameters:
        - task_tree: Reference to the Treeview widget
        - task_manager: TaskManager instance
        - refresh_callback: Function to update the display
        """
        self.task_tree = task_tree
        self.task_manager = task_manager
        self.refresh_callback = refresh_callback

    def execute(self):
        """Main entry point for deletion process"""
        selected_items = self._get_selected_items()
        if not selected_items:
            return

        if self._confirm_deletion():
            self._perform_deletion(selected_items)
            self.refresh_callback()

    def _get_selected_items(self):
        """Returns list of selected item IDs or shows warning"""
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task to delete!")
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
