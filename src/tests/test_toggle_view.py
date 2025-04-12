import unittest
from tkinter import Tk, ttk
from ..gui.calendar_view import CalendarView
from ..gui.toggle_view import ToggleViewHandler
from ..cli.task_manager import TaskManager

class TestToggleViewHandler(unittest.TestCase):
    def setUp(self):
        """Set up a Tkinter root, TaskManager, CalendarView, and Treeview for testing."""
        self.root = Tk()
        self.task_manager = TaskManager()
        self.calendar_view = CalendarView(self.root, self.task_manager)

        self.treeview = ttk.Treeview(self.root)
        self.treeview.grid()

        self.toggle_handler = ToggleViewHandler(self.treeview, self.calendar_view)

        self.root.update()

    def tearDown(self):
        """Destroy the Tkinter root after each test."""
        self.root.destroy()

    def test_toggle_to_calendar_view(self):
        """Test toggling from Treeview to CalendarView."""
        self.assertTrue(self.treeview.winfo_ismapped())
        self.assertFalse(self.calendar_view.frame.winfo_ismapped())

        self.toggle_handler.toggle()
        self.root.update()

        self.assertFalse(self.treeview.winfo_ismapped())
        self.assertTrue(self.calendar_view.frame.winfo_ismapped())

    def test_toggle_to_treeview(self):
        """Test toggling from CalendarView to Treeview."""
        self.toggle_handler.toggle()

        self.assertFalse(self.treeview.winfo_ismapped())

        self.toggle_handler.toggle()
        self.root.update()

        self.assertTrue(self.treeview.winfo_ismapped())

if __name__ == "__main__":
    unittest.main()