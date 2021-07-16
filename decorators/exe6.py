import random
import functools

def retry(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'Retrying ({e})')
        return wrapper
    return decorator

@retry(max_retries = 3)
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number

only_roll_sixes()
