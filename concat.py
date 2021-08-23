from __future__ import annotations

class Concatable():
    def __concat(left, right):
        if not callable(right):
            if type(right) == tuple:
                return left(*right)
            return left(right)

        return Concatable(lambda *args: left(right(*args)))
    
    
    def __init__(self, concatted):
        self.concatted = concatted
    
    
    def __lshift__(self, right):
        return Concatable.__concat(self.concatted, right)
    
    
    def __rlshift__(self, left):
        return Concatable.__concat(left, self.concatted)


APPLY = Concatable(lambda _: _)