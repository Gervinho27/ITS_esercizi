#Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:
#tutti i numeri pari vengano prima di tutti i numeri dispari;
#l’ordine relativo tra pari e dispari va mantenuto;
#l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.
#esempio: print(even_odd_pattern([3, 6, 1, 8, 4, 7]))

def even_odd_pattern(number:list[int]) -> list[int]:
    even_numbers = [num for num in number if num % 2 == 0]
    odd_numbers = [num for num in number if num % 2 != 0]
    return even_numbers + odd_numbers
