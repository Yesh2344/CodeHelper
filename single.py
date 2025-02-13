# single.py
import datetime

class Singleton(type):
    """
    A metaclass for implementing the Singleton design pattern.
    Ensures that only one instance of a class is created.
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"Creating a new instance of {cls.__name__}.")
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            print(f"Using existing instance of {cls.__name__}.")
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    """
    A simple Logger class implemented as a Singleton.
    Logs messages with timestamps to a file and the console.
    """
    def __init__(self, log_file="app.log"):
        self.log_file = log_file
        # Initialize the log file with a header.
        with open(self.log_file, "w") as f:
            f.write(f"Logger started at {datetime.datetime.now()}\n")

    def log(self, message):
        """
        Logs a message with a timestamp.
        """
        timestamp = datetime.datetime.now().isoformat()
        log_message = f"[{timestamp}] {message}"
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")
        print(log_message)
