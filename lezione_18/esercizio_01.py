import math

def safe_sqrt(number):
    try:
        return math.sqrt(number)
    except ValueError:
        return "Non puoi calcolare la radice quadrata di un numero negativo."
    
print(safe_sqrt(16))
print(safe_sqrt(-4))