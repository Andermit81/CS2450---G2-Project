from ..cli.task import Task
from ..cli.task_manager import TaskManager
from ..gui.task_visualizer import TaskVisualizer
import unittest
import matplotlib
matplotlib.use('Agg')  

class TestTaskVisualizer(unittest.TestCase):
    def setUp(self):
        """Set up a TaskManager instance and sample tasks for testing"""
        self.task_manager = TaskManager()
        self.visualizer = TaskVisualizer(self.task_manager)
        
        # Create test tasks
        self.completed_task = Task(
            title="Completed Task",
            description="This task is done",
            tags=["Done", "Important"]
        )
        self.incomplete_task = Task(
            title="Incomplete Task",
            description="This task needs work",
            tags=["Work"]
        )
        self.untagged_task = Task(
            title="Untagged Task",
            description="No tags here"
        )
        
        self.task_manager.add_task(self.completed_task)
        self.task_manager.add_task(self.incomplete_task)
        self.task_manager.add_task(self.untagged_task)

    def test_get_completion_data(self):
        """Test that completion data is calculated correctly"""
        completed, incomplete = self.visualizer.get_completion_data()
        self.assertEqual(completed, 1)  # Only one task has "Done" tag
        self.assertEqual(incomplete, 2)  # Two tasks without "Done" tag

    def test_empty_task_manager(self):
        """Test visualization with no tasks"""
        empty_manager = TaskManager()
        empty_visualizer = TaskVisualizer(empty_manager)
        completed, incomplete = empty_visualizer.get_completion_data()
        self.assertEqual(completed, 0)
        self.assertEqual(incomplete, 0)

    def test_pie_chart_data(self):
        """Test that pie chart data is generated correctly"""
        # Mock the figure creation
        fig = self.visualizer.create_pie_chart(None)
        
        # For Agg backend, we can't test the widget, but we can verify the data
        completed, incomplete = self.visualizer.get_completion_data()
        self.assertEqual(completed, 1)
        self.assertEqual(incomplete, 2)

    def test_tag_changes_affect_completion(self):
        """Test that changing tags updates completion status"""
        # Initially 1 completed, 2 incomplete
        completed, incomplete = self.visualizer.get_completion_data()
        self.assertEqual(completed, 1)
        self.assertEqual(incomplete, 2)
        
        # Mark incomplete task as done
        self.incomplete_task.tags.append("Done")
        completed, incomplete = self.visualizer.get_completion_data()
        self.assertEqual(completed, 2)
        self.assertEqual(incomplete, 1)
        
        # Remove done tag from completed task
        self.completed_task.tags.remove("Done")
        completed, incomplete = self.visualizer.get_completion_data()
        self.assertEqual(completed, 1)
        self.assertEqual(incomplete, 2)

if __name__ == "__main__":
    unittest.main()
