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

@timethis
def countdown(n):
    while n > 0:
        n -= 1

def countdown_copy(n):
    while n > 0:
        n -= 1

# traditional method
countdown(10000000)

# equivalent method
cd = timethis(countdown_copy)
cd(10000000)