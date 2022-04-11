import time
from functools import wraps

def timethis(func):
    '''Decorator that reports the execution time'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end-start}")
        return result
    return wrapper

def timethis_without_wraps(func):
    '''Decorator that reports the execution time'''

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end-start}")
        return result
    return wrapper

@timethis
def countdown(n:int):
    '''Countdown doc'''
    while n > 0:
        n -= 1

@timethis_without_wraps
def countdown_copy(n:int):
    '''Countdown_copy doc'''
    while n > 0:
        n -= 1

# preserve metadata
countdown(10000000)
print(f"{countdown.__name__}")
print(f"{countdown.__doc__}")
print(f"{countdown.__annotations__}")

# lose metadata
countdown_copy(10000000)
print(f"{countdown_copy.__name__}")
print(f"{countdown_copy.__doc__}")
print(f"{countdown_copy.__annotations__}")

# access wrapped function (countdown) directly
# only run, no print
countdown.__wrapped__(10000000)