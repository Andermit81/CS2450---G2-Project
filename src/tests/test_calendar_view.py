import unittest
from tkinter import Tk
from datetime import datetime
from ..cli.task import Task
from ..cli.task_manager import TaskManager
from ..gui.calendar_view import CalendarView

class TestCalendarView(unittest.TestCase):
    def setUp(self):
        """Set up a Tkinter root, TaskManager, and CalendarView for testing."""
        self.root = Tk()
        self.task_manager = TaskManager()
        self.calendar_view = CalendarView(self.root, self.task_manager)

        self.task_manager.tasks.clear()
        
        self.task1 = Task(title="Task 1", due_date="2025-04-15", priority="High")
        self.task2 = Task(title="Task 2", due_date="2025-04-15", priority="Medium")
        self.task3 = Task(title="Task 3", due_date="2025-04-16", priority="Low")
        self.task_manager.add_task(self.task1)
        self.task_manager.add_task(self.task2)
        self.task_manager.add_task(self.task3)

    def tearDown(self):
        """Destroy the Tkinter root after each test."""
        self.root.destroy()

    def test_get_tasks_for_date(self):
        """Test that tasks are correctly retrieved for a specific date."""
        tasks = self.calendar_view.get_tasks_for_date("2025-04-15")
        self.assertEqual(len(tasks), 2)
        print(tasks)
        self.assertIn(self.task1, tasks)
        self.assertIn(self.task2, tasks)

    def test_on_date_select(self):
        """Test that tasks are displayed in the Listbox for the selected date."""
        self.calendar_view.on_date_select(None)
        self.calendar_view.calendar.selection_set("2025-04-15")
        self.calendar_view.on_date_select(None)

        listbox_items = self.calendar_view.task_list.get(0, "end")
        self.assertIn("Task 1 - High", listbox_items)
        self.assertIn("Task 2 - Medium", listbox_items)

    def test_get_selected_task_id(self):
        """Test that the correct task ID is returned for a selected Listbox item."""
        self.calendar_view.on_date_select(None)
        self.calendar_view.calendar.selection_set("2025-04-15")
        self.calendar_view.on_date_select(None)

        self.calendar_view.task_list.selection_set(0)
        selected_task_id = self.calendar_view.get_selected_task_id()
        self.assertEqual(selected_task_id, self.task1.task_id)

if __name__ == "__main__":
    unittest.main()