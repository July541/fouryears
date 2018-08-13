from threading import Lock

def synchronized(function):
    function.__lock__ = Lock()
    
    def synced_func(*args, **kwargs):
        with function.__lock__:
            return function(*args, **kwargs)

    return synced_func

def singleton(cls):
    instances = {}
    
    @synchronized
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance