from functools import wraps
from datetime import datetime

SUPPRESS_TIME_DECORATOR = True  # Set this to True to suppress the decorator, False to enable it

def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if SUPPRESS_TIME_DECORATOR:
            return func(*args, **kwargs)
        print(f"{func.__name__}", end=" ", flush=True)
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        duration = end - start
        duration_rounded = round(duration.total_seconds() * 1000) / 1000
        print(f"executed in {duration_rounded} seconds")
        return result
    return wrapper
