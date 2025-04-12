from tkcalendar import Calendar
from tkinter import Frame, Label, Listbox
from datetime import datetime

class CalendarView:
    def __init__(self, parent, task_manager, bg_color="#F5F7FA", text_color="black"):
        """
        Initializes the CalendarView with a parent widget, task manager, background color, and text color.
        parent: The parent widget where the calendar will be placed.
        task_manager: The TaskManager instance to manage tasks.
        bg_color: Background color of the calendar.
        text_color: Text color of the calendar.
        """
        self.parent = parent
        self.task_manager = task_manager
        self.bg_color = bg_color
        self.text_color = text_color
        self.task_id_map = {}

        # Create a frame for the calendar view
        self.frame = Frame(self.parent, bg=self.bg_color)

        # Create the calendar widget
        self.calendar = Calendar(self.frame, selectmode="day", date_pattern="yyyy-mm-dd", font=("Arial", 16), headersbackground="#1ABC9C")
        self.calendar.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Add a listbox to display tasks
        self.task_list = Listbox(self.frame, bg=self.bg_color, fg=self.text_color, height=12, font=("Arial", 12), selectbackground="#34495E", activestyle="none")
        self.task_list.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Configure grid weights for resizing
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        # Bind the calendar to show tasks for the selected day
        self.calendar.bind("<<CalendarSelected>>", self.on_date_select)

    def show(self):
        """Displays the calendar view."""
        self.frame.grid(row=0, column=0, columnspan=5, sticky="nsew")
        self.calendar.selection_clear()
        self.task_list.config(state="normal")
        self.task_list.delete(0, "end")
        self.task_list.insert("end", "Select a date to view tasks")
        self.task_list.configure(fg="lightgray", font=("Arial", 12, "italic"))
        self.task_list.config(state="disabled")

    def hide(self):
        """Hides the calendar view."""
        self.frame.pack_forget()

    def highlight_task_days(self):
        """Highlights the days with tasks in the calendar."""
        selected_date = self.calendar.get_date()
        self.calendar.calevent_remove("all")

        tasks_by_date = {}
        for task_id, task in self.task_manager.tasks.items():
            if task.due_date:
                if isinstance(task.due_date, str):
                    try:
                        task_date = datetime.strptime(task.due_date, "%Y-%m-%d").date()
                    except ValueError:
                        print(f"Invalid date format for task {task_id}: {task.due_date}")
                        continue
                else:
                    task_date = task.due_date

                if task_date not in tasks_by_date:
                    tasks_by_date[task_date] = []
                tasks_by_date[task_date].append(task)

        for task_date, tasks in tasks_by_date.items():
            all_done = all("Done" in task.tags for task in tasks)

            if all_done:
                self.calendar.calevent_create(task_date, "All tasks done", "task_done")
            else:
                self.calendar.calevent_create(task_date, "Tasks pending", "task_due")    

        self.calendar.tag_config("task_done", background="#D4EDDA", foreground="#155724")
        self.calendar.tag_config("task_due", background="#fffacc", foreground="#6e6300")

        if selected_date:
            try:
                self.calendar.selection_set(selected_date)
            except ValueError:
                pass

    def on_date_select(self, event):
        """Displays tasks for the selected date."""
        selected_date = self.calendar.get_date()
        tasks = self.get_tasks_for_date(selected_date)

        self.task_list.config(state="normal")
        self.task_list.delete(0, "end")
        self.task_id_map.clear()

        if not tasks:
            self.task_list.insert("end", "No tasks for this date")
            self.task_list.configure(fg="lightgray", font=("Arial", 12, "italic"))
            self.task_list.selection_clear(0, "end")
            self.task_list.config(state="disabled") 
        else:
            self.task_list.configure(fg=self.text_color, font=("Arial", 12))
            for index, task in enumerate(tasks):
                task_text = f"{task.title} - {task.priority}"
                if "Done" in task.tags:
                    task_text += " (Done)"
                    self.task_list.insert("end", task_text)
                    self.task_list.itemconfig("end", bg="#D4EDDA", fg="#155724")
                else:
                    self.task_list.insert("end", task_text)
                    self.task_list.itemconfig("end", bg="#ECF0F1")

                self.task_id_map[index] = task.task_id


    def get_tasks_for_date(self, date):
        """Retrieves tasks for a specific date."""
        tasks_for_date = []
        for task_id, task in self.task_manager.tasks.items():
            if task.due_date == date and task_id not in [t.task_id for t in tasks_for_date]:
                tasks_for_date.append(task)
        return tasks_for_date
    
    def get_selected_task_id(self):
        selected_index = self.task_list.curselection()
        if not selected_index:
            return None
        return self.task_id_map.get(selected_index[0])