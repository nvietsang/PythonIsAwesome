import logging
from functools import wraps

logging.basicConfig(level=logging.DEBUG)

def logged(level, name=None, message=None):
    '''
    Add logging to a function.
    level is the logging level,
    name is the logger name,
    and message is the log message.
    If name and message aren't specified, they default to the function's module and name.
    '''

    def decorate(func):
        logname = name if name else func.__module__
        logger = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print("Spam!")



add(3, 4)
spam()