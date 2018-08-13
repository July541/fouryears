from abc import ABCMeta, abstractmethod

class ITask(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def logic(self):
        pass