# La funzione dovrebbe determinare se un elemento è presente in una lista.
# Un errore nell'implementazione porta a risultati inaspettati.
 
# TROVA L'ERRORE E CORREGGI IL CODICE

# def find_element(lst: list[int], element: int) -> bool:
#     for item in lst:
#         if item == element:
#             return True
#     return False                    questo return deve essere fuori dal ciclo for



# Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
# For example:
# print(sum_above_threshold([15, 5, 25], 20))  risulatato 25

# def sum_above_threshold(numbers: list[int], ...) -> int:
      # prima cancella ... e definisci parametro e tipo per il dato mancante
      # successivamente cancella pass e scrivi il tuo codice
#     pass

#def sum_above_threshold(numbers: list[int], threshold: int) -> int:
#     total = 0
#     for number in numbers:
#         if number > threshold:
#             total += number
#     return total
# print(sum_above_threshold([15, 5, 25], 20))
# print(sum_above_threshold([1, 10, 20, 30], 10))





# Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione.'
# 'L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
# For example:
# print(check_combination(True, False, True))
# Operazione permessa

# print(check_combination(False, True, False))
# Operazione negata

# def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
#     if conditionA or (conditionB and conditionC):
#         return "Operazione permessa"
#     else:
#         return "Operazione negata"

# def countdown(number: int) -> None:
#     while number >= 0:
#         print(number)
#         number -= 1
# countdown(5)





#Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit.
#Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
#For example:
#print(convert_temperature(0))
#32.0

#print(convert_temperature(32, False))
#0.0

#def convert_temperature(temperature: float, to_fahrenheit: bool = True) -> float:
#    if to_fahrenheit:
#        return temperature + 32 * 9/5
#    else:
#        return temperature - 32 * 5/9
#print(convert_temperature(0))
#print(convert_temperature(32, False))


#Scrivi una funzione che unisce due dizionari.
#Se una chiave è presente in entrambi, somma i loro valori.
#For example:
#print(merge_dictionaries({'x': 5}, {'x': -5}))
#{'x': 0}

#def merge_dictionaries(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
#    merged_dict = dict1.copy()
#    for key, value in dict2.items():
#        if key in merged_dict:
#            merged_dict[key] += value
#        else:
#            merged_dict[key] = value
#    return merged_dict



#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
#For example:
#print(remove_elements({5, 6, 7}, [7, 8, 9]))
#{5, 6}

#def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
#return original_set - set(elements_to_remove)