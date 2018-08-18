from abc import ABCMeta, abstractmethod

class IConfigReader(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, config):
        self.config_file = config

    @abstractmethod
    def get_value(self, key):
        pass

    