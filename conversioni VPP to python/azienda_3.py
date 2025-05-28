import re
from datetime import *
from esercizio_tipo_di_dato import Indirizzo, Telefono

class RealGEZ:
    def __new__(cls, valore: int | float):
        if valore < 0:
            return super().__new__()
        raise ValueError("Lo stipendio non può essere negativo.")

class Impiegato:
    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ):
        self.nome =nome
        self.cognome = cognome
        self.nascita = nascita
        self.stipendio = stipendio

    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, new_nome: str)-> None:
        self.nome = new_nome

    def get_cognome(self) -> str:
        return self.cognome
    
    def set_cognome(self, new_cognome: str) -> None:
        self.cognome = new_cognome

    def get_nascita(self) -> datetime.date:
        return self.nascita
    
    def get_stipendio(self) -> RealGEZ:
        return self.stipendio
    
    def set_stipendio(self, new_stipendio: RealGEZ) -> None:
        self.stipendio = new_stipendio

class Dipartimento:
    def __init__(self, nome : str, telefono: Telefono, idirizzo: Indirizzo):
        self.nome = nome
        self.telefono = set[Telefono]
        self.indirizzo = Indirizzo

    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, new_nome: str) -> None:
        self.nome = new_nome

    def get_telefono(self) -> frozenset[Telefono]:
        return self.telefono
    
    def add_telefono(self, new_telefono: Telefono) -> None:
        self.telefono.add(new_telefono)

    def remove_telefono(self, telefono: Telefono) -> None:
        if len(self.telefono()) > 1:
            self.telefono.remove(telefono)
        raise ValueError("CImpossibile rimuovere, ci deve essere per forza un numero.")
    
    def get_indirizzo(self) -> Indirizzo:
        return self.indirizzo
    
    def set_indirizzo(self, new_indirizzo: Indirizzo) -> None:
        self.indirizzo = new_indirizzo  
        
class Progetto:
    def __init__(self, nome: str, budget: RealGEZ):
        self.nome = nome
        self.budget = budget

    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, new_nome: str) -> None:
        self.nome = new_nome

    def get_budget(self) -> RealGEZ:
        return self.budget
    
    def set_budget(self, new_budget: RealGEZ) -> None:
        self.budget = new_budget