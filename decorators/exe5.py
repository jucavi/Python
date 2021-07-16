import functools
import random

def retry(exception):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    print(f'Retrying ({e})')
        return wrapper
    return decorator

@retry(ValueError)
def calculation():
    number = random.randint(-5, 5)
    if abs(1 / number) > 0.2:
        raise ValueError(number)
    return number

calculation() # -5, 5, or ZeroDivisionError