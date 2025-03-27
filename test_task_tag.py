from task import Task
from task_manager import TaskManager
import unittest

class TestTaskTags(unittest.TestCase):
    def setUp(self):
        """Set up a TaskManager instance and sample tasks for testing."""
        self.task_manager = TaskManager()
        self.task1 = Task(
            title="Test Task",
            description="This is a test task.",
            due_date="2023-12-31",
            priority="High",
            tags=["xyz", "abc", "123"]
        )
        self.task2 = Task(
            title="Another Task",
            description="This is another test task.",
            due_date="2023-11-30",
            priority="Medium",
            tags=["Work", "Project", "Urgent"]
        )
        self.task_manager.add_task(self.task1)
        self.task_manager.add_task(self.task2)

    def test_add_task(self):
        """Test adding tasks to the TaskManager."""
        self.assertEqual(len(self.task_manager.tasks), 2)
        self.assertIn(self.task1.task_id, self.task_manager.tasks)
        self.assertIn(self.task2.task_id, self.task_manager.tasks)

    def test_view_tasks(self):
        """Test the view_tasks method."""
        output = self.task_manager.view_tasks()
        self.assertIn("Test Task", output)
        self.assertIn("Another Task", output)
        self.assertIn("123, abc, xyz", output)  # Check if tags are displayed
        self.assertIn("Project, Urgent, Work", output)

    def test_save_and_load_tasks(self):
        """Test saving and loading tasks."""
        self.task_manager.save_tasks()
        self.task_manager.tasks = {}  # Clear tasks to simulate a fresh load
        self.task_manager.load_tasks()

        # Verify tasks are loaded correctly
        self.assertEqual(len(self.task_manager.tasks), 2)
        loaded_task1 = self.task_manager.tasks[self.task1.task_id]
        loaded_task2 = self.task_manager.tasks[self.task2.task_id]

        self.assertEqual(loaded_task1.title, "Test Task")
        self.assertEqual(loaded_task1.tags, ["xyz", "abc", "123"])
        self.assertEqual(loaded_task2.title, "Another Task")
        self.assertEqual(loaded_task2.tags, ["Work", "Project", "Urgent"])

    def test_tags_are_sorted(self):
        """Test that tags are displayed in alphabetical order."""
        output = self.task_manager.view_tasks()
        self.assertIn("123, abc, xyz", output)  # Tags should be sorted alphabetically
        self.assertIn("Project, Urgent, Work", output)

if __name__ == "__main__":
    unittest.main()