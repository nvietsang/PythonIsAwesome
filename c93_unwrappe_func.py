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
def add(x, y):
    return x + y

orig_add = add.__wrapped__

print(add(3, 4))
print(orig_add(3, 4))
