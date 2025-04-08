#Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista.
#Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.
#Il tuo compito è individuare i numeri mancanti.
#Scrivi una funzione che, data in input una lista, restituisca una nuova lista ordinata contenente tutti i numeri da 1 a n che non sono presenti nella lista originale.
#es: print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))


def find_disappeared_numbers(nums:list[int]) -> list[int]:
        n = len(nums)
        completa_set = set(range(1, n + 1))
        nums_set = set(nums)
        missing_numbers = completa_set - nums_set
        return sorted(missing_numbers)  