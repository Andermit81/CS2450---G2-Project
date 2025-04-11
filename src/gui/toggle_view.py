from .calendar_view import CalendarView

class ToggleViewHandler:
    def __init__(self, task_tree, calendar_view):
        """
        Initializes the ToggleViewHandler with the task tree and calendar view.
        task_tree: The Treeview widget for the tabular view.
        calendar_view: The CalendarView instance for the calendar view.
        """
        self.task_tree = task_tree
        self.calendar_view = calendar_view

    def toggle(self):
        """Toggles between the tabular view and calendar view."""
        if self.task_tree.winfo_ismapped():
            # Switch to calendar view
            self.task_tree.grid_remove()
            self.calendar_view.show()
            self.calendar_view.highlight_task_days()
        else:
            # Switch to tabular view
            self.calendar_view.hide()
            self.task_tree.grid()

            