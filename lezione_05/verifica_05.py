#Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
#La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.

def somma_elementi(x : list[int], y : list[int]) -> list[int]:
    risultato = []
    for i in range(len(x)):
        risultato.append(x[i] + y[i])
    return risultato