import functools
from os import fstatvfs, path
import random

class Retry:
    def __init__(self, func):
        self.func = func
        self.num_retries = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        while True:
            try:
                return self.func(*args, **kwargs)
            except Exception as e:
                self.num_retries += 1
                print(f'Retry attempt {self.num_retries}')
            

@Retry
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number 

only_roll_sixes()