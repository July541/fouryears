from multiprocessing import Process
from singleton import singleton

from task import Task

@singleton
class Parallel:
    def __init__(self):
        self.process = None

    def run(self, task, args=None):
        self.process = Process(target=task)
        self.process.start()
        self.process.join()