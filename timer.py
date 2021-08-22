from time import time
from typing import Callable

def timing(f: Callable):
    def measure_time(*args, **kwargs):
        time1 = time()
        returned_value = f(*args, **kwargs)
        time2 = time()
        print('function took {:.3f} ms'.format((time2-time1)*1000.0))

        return returned_value
    
    return measure_time


@timing
def measure_time(func: Callable):
    func()
    