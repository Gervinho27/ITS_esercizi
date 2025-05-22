from functools import reduce
lista_numeri = [2, 3, 4]
prodotto = reduce(lambda x, y : x * y, lista_numeri)
print(prodotto)