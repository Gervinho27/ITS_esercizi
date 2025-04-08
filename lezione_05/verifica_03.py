#Scrivi una funzione che calcoli i fattori primi di un numero intero positivo n.

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

print(prime_factors(4))   # Output: [2, 2]
print(prime_factors(60))  # Output: [2, 2, 3, 5]
