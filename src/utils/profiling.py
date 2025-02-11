import time
from functools import wraps
from typing import Callable, Any
from memory_profiler import profile as memory_profile

def timing_decorator(func: Callable) -> Callable:
    """Decorator to measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {(end_time - start_time) * 1000:.2f}ms")
        return result
    return wrapper

# Memory profiling decorator
profile_memory = memory_profile

# Example usage:
# @timing_decorator
# @profile_memory
# def your_function():
#     pass 