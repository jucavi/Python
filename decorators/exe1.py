import functools

def before_and_after(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        print('BEFORE')
        func(*args, **kargs)
        print('AFTER')
    return wrapper

@before_and_after
def greet(name):
    print(f'Hi {name}!')

greet('PyCon')