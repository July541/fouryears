from threading import Timer

from parallel import Parallel
from task import Task

MAX_THREAD_NUM = 5

class Observer:
    def __init__(self):
        self.frequency = 0
        self.task = None

    def update_task(self, task:Task):
        self.task = task

    def do_task(self):
        if self.task != None:
            p = Parallel()
            print(p)
            Parallel().run(self.task.logic)

    def observe(self, frequency:int, cond):
        tm = Timer(frequency, self.observe, (frequency, cond))
        tm.start()
        if cond:
            self.do_task()