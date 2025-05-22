import matplotlib.pyplot as plt

def Collatz (n : float) -> list[float]:

    numbers : list = [n]

    while n != 1:
        
        if n % 2 == 0:
            
            n = n / 2
        
        else:
            n = 3 * n + 1
        
        numbers.append(n)

    return numbers

numeri : list[float] = Collatz(8.0)
plt.plot(numeri)
plt.show()