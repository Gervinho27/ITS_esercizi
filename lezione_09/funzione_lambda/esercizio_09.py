def moltiplicatore(n):
    return lambda x : x * n

moltiplica_per_10 = moltiplicatore(10)
prodotto = moltiplica_per_10(5)
print(prodotto)