from typing import Callable
sum : Callable[[int, int], int] = lambda x, y: x + y
print(sum(10, 72))

print(sum(15, 78))