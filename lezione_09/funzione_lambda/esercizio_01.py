from typing import Callable
square:Callable[[int], int] = lambda x: x ** 2
print(square(5))

def square(x: int) -> int:
    return x ** 2
print(square(10))