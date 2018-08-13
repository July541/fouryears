from ITask import ITask
from tasktype import TaskType

class Task(ITask):
    def __init__(self):
        self.task_type = None # str
        self.imp = None
        self.cb = None
        
    def logic(self):
        self.imp()

    def set_task(self, func, task_type = TaskType.Unknown, callback = None):
        self.imp = func
        self.task_type = task_type
        self.cb = callback