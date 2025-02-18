# test_task.py
import unittest
from task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        """Create sample tasks for testing."""
        self.minimal_task = Task(title="Learn Python")
        self.full_task = Task(
            title="Finish project",
            description="Complete the CLI prototype",
            due_date="2023-12-31",
            priority="High"
        )

    # -------------------------------------------------------------------------
    # Test Initialization
    # -------------------------------------------------------------------------
    def test_initialization_with_all_fields(self):
        """Test that all fields are correctly initialized."""
        self.assertEqual(self.full_task.title, "Finish project")
        self.assertEqual(self.full_task.description, "Complete the CLI prototype")
        self.assertEqual(self.full_task.due_date, "2023-12-31")
        self.assertEqual(self.full_task.priority, "High")
        self.assertIsInstance(self.full_task.task_id, str)  # ID should be a string

    def test_default_values(self):
        """Test that optional fields use defaults when not provided."""
        self.assertEqual(self.minimal_task.description, "")
        self.assertIsNone(self.minimal_task.due_date)
        self.assertEqual(self.minimal_task.priority, "Medium")
        self.assertIsInstance(self.minimal_task.task_id, str)

    # -------------------------------------------------------------------------
    # Test Equality
    # -------------------------------------------------------------------------
    def test_equality(self):
        """Two different tasks should NOT be equal (different IDs)."""
        task1 = Task(title="Task 1")
        task2 = Task(title="Task 2")
        self.assertNotEqual(task1, task2)

    def test_equality_with_same_instance(self):
        """A task should be equal to itself."""
        self.assertEqual(self.minimal_task, self.minimal_task)

    def test_equality_with_non_task_object(self):
        """A task should not be equal to a non-Task object."""
        self.assertNotEqual(self.minimal_task, "Not a task")

    # -------------------------------------------------------------------------
    # Test ID Uniqueness
    # -------------------------------------------------------------------------
    def test_task_id_uniqueness(self):
        """Auto-generated task IDs should be unique."""
        task1 = Task(title="Task 1")
        task2 = Task(title="Task 2")
        self.assertNotEqual(task1.task_id, task2.task_id)

    # -------------------------------------------------------------------------
    # Test String Representation
    # -------------------------------------------------------------------------
    def test_repr(self):
        """__repr__ should return a developer-friendly string."""
        expected_repr = (
            f"Task(title='Learn Python', "
            f"description='', due_date='None', "
            f"priority='Medium', task_id='{self.minimal_task.task_id}')"
        )
        self.assertEqual(repr(self.minimal_task), expected_repr)

if __name__ == "__main__":
    unittest.main()