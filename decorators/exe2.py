import random
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        return func(*args, **kargs), func(*args, **kargs)
    return wrapper

@do_twice
def roll_dice():
    return random.randint(1,6)

print(roll_dice())