import unittest
from task import Task
from task_manager import TaskManager
from copy import deepcopy

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Create a TaskManager and sample tasks for testing."""
        self.manager = TaskManager()
        self.task1 = Task(title="Learn Python")
        self.task2 = Task(title="Finish project")

    # -------------------------------------------------------------------------
    # Test Adding Tasks
    # -------------------------------------------------------------------------
    def test_add_task(self):
        """Test adding a task to the manager."""
        self.manager.add_task(self.task1)
        self.assertIn(self.task1.task_id, self.manager.tasks)
        self.assertEqual(self.manager.tasks[self.task1.task_id], self.task1)

    def test_add_duplicate_task(self):
        """Adding a task with the same ID should raise an error."""
        self.manager.add_task(self.task1)
        with self.assertRaises(ValueError):
            self.manager.add_task(self.task1)  # Same task, same ID

    # -------------------------------------------------------------------------
    # Test Removing Tasks
    # -------------------------------------------------------------------------
    def test_remove_task(self):
        """Test removing a task from the manager."""
        self.manager.add_task(self.task1)
        self.manager.remove_task(self.task1.task_id)
        self.assertNotIn(self.task1.task_id, self.manager.tasks)

    def test_remove_nonexistent_task(self):
        """Removing a non-existent task should raise an error."""
        with self.assertRaises(ValueError):
            self.manager.remove_task("invalid-id")

    # -------------------------------------------------------------------------
    # Test Viewing Tasks
    # -------------------------------------------------------------------------
    def test_view_tasks_empty(self):
        """Test view_tasks when no tasks exist."""
        expected_output = "No tasks available."
        self.assertEqual(self.manager.view_tasks(), expected_output)

    def test_view_tasks(self):
        """Test that view_tasks returns the correct task information."""
        self.manager.add_task(self.task1)
        self.manager.add_task(self.task2)
    
        output = self.manager.view_tasks()
    
        # Just check if task titles exist in the output
        self.assertIn(self.task1.title, output)
        self.assertIn(self.task2.title, output)

    # -------------------------------------------------------------------------
    # Test Task Dictionary Integrity
    # -------------------------------------------------------------------------
    def test_task_dictionary_integrity(self):
        """Ensure the tasks dictionary updates correctly."""
        self.manager.add_task(self.task1)
        self.manager.add_task(self.task2)
        self.assertEqual(len(self.manager.tasks), 2)
        self.assertIn(self.task1.task_id, self.manager.tasks)
        self.assertIn(self.task2.task_id, self.manager.tasks)
        
    # -------------------------------------------------------------------------
    # Test Proper Save/Load
    # -------------------------------------------------------------------------
    def test_save_load(self):
        """Test that the tasks correctly save and load"""
        manager_copy = deepcopy(self.manager)
        self.manager.save_tasks()
        self.manager.load_tasks()
        self.assertEqual(self.manager.tasks, manager_copy.tasks)
    

if __name__ == "__main__":
    unittest.main()
