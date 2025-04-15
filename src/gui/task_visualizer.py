import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from ..cli.task_manager import TaskManager

TASK_AREA_BG = "#ECF0F1"

class TaskVisualizer:
    """A class for visualizing task completion data using a pie chart"""
    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager

    def get_completion_data(self):
        """Returns counts of completed and incomplete tasks"""
        completed = 0
        incomplete = 0
        
        for task in self.task_manager.tasks.values():
            if "Done" in task.tags:
                completed += 1
            else:
                incomplete += 1
        return completed, incomplete

    def create_pie_chart(self, master_frame):
        """Creates and returns a pie chart widget"""
        completed, incomplete = self.get_completion_data()
        
        if completed + incomplete == 0:
            # Return a label if no tasks exist
            no_tasks_label = tk.Label(master_frame, text="No current tasks", 
                                    font=('Arial', 12), bg=TASK_AREA_BG)
            return no_tasks_label
        
        # Create figure and plot
        fig = plt.figure(figsize=(4, 3), dpi=80, facecolor=TASK_AREA_BG)
        ax = fig.add_subplot(111)
        
        labels = ['Completed', 'Incomplete']
        sizes = [completed, incomplete]
        colors = ['#1ABC9C', '#E74C3C']  # Green and red
        explode = (0.1, 0)  # Slightly highlight the completed slice
        
        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=140)
        ax.axis('equal')  # Equal aspect ratio
        ax.set_title('Task Completion Status', pad=10)

        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=master_frame)
        canvas.draw()
        return canvas.get_tk_widget()
