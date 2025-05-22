n = int(input("Inserisci un numero: "))

def numeroprimo(n):

    
    if n < 2:
        print(f"{n} non è un numero primo!")
        return False
    
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} non è un numero primo")
            return False
        
    if True:
        print(f"{n} è un numero primo!")
    else:
        print(f"{n} non è un numero primo!")

print(numeroprimo(n))