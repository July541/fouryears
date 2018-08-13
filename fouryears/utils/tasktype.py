from enum import Enum, unique

@unique
class TaskType(Enum):
    Unknown = -1
    Others = 1
    SendByEmail = 2