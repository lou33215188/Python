import time,functools

def log(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('begin call')
        c=fn(*args,**kw)
        print('end call')
        return c
    return wrapper

@log
def now():
    print('Hello!')

print(now())
