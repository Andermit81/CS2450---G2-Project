import uuid # module to help create unique IDs

# Task class to be instantiated to represent individual tasks
class Task:
    def __init__(
        self, # refrence to the instance being created
        title: str,
        description: str = "", # "" makes the description optional, sets default to empty string
        due_date: str = None, # optional dude date
        priority: str = "Medium", # default priority set to Medium, but can be changed by user
        tags: list[str] = None, # Optional list of tag
    ):
        # initializing instance attributes
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.task_id = str(uuid.uuid4())  # Will always generate a custom ID
        self.tags = tags if tags else []

    # just for console output debugging
    def __repr__(self):
        # Returns a string like "Task(title='...', ...) so we can see it in a readable format"
        return (
            f"Task(title='{self.title}', "
            f"description='{self.description}', "
            f"due_date='{self.due_date}', "
            f"priority='{self.priority}', "
            f"task_id='{self.task_id}')"
        )

    # Equality check for tasks
    def __eq__(self, other):
        # Checks equality based on task_id
        if not isinstance(other, Task):
            return False
        return self.task_id == other.task_id