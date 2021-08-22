from typing import Callable, Iterable
from functools import partial
from itertools import takewhile, count

def infinity_from(x):
    yield from count(x)
    
 
def filter_divisable_by(denominator: float) -> Callable[[Iterable], Iterable]:
    def is_divisible(item: float) -> bool:
        return not bool(item % denominator)
    
    return partial(filter, is_divisible)

        
def until(max: float) -> Callable[[Iterable], Iterable]:
    def hasnt_reached_maximum(item: float) -> bool:
        return item <= max
    
    return partial(takewhile, hasnt_reached_maximum)

def get_n_items(num: int):
    def hasnt_called_n_times(_):
        nonlocal num
        num -= 1
        return num >= 0
    
    return partial(takewhile, hasnt_called_n_times)


def power_by(exponent: float): 
    def power(item: float):
        return item ** exponent
    
    return partial(map, power)
