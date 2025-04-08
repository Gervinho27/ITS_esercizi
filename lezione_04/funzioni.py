def add(a, b):
    return a + b
print(add(2, 3))

mylist = ["a", "b", "c"]
print(mylist)
print(*mylist)

mytuple = (1, 2, 3, 4, 5)
print(mytuple)
print(*mytuple)

def myfunc(*args):
    print(args)
    print(type(args))
myfunc(1, 2, 3, 4, 5)

def add(*args): # Accepts multiple numbers in input
    total = 0
    for number in args:
        total += number
    return total
print(add(2, 3)) # Output 5
print(add(10, 20, 30)) # Output 60

def total_price(*args):
    total:float = sum(args)
    return total
print(total_price(2.99, 4.55, 2.99)) # Works, but what are these prices?

#So, we need to use **kwargs to pass key-value pairs (name and price)

def myfunc(**kwargs):
    print(kwargs)
    print(type(kwargs))
myfunc(coffe=2.99, cake=4.55, juice=2.99)
