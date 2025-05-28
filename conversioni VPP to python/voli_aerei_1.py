import re
from datetime import *

class Nazione:
    def __init__(self, nome : str):
        self._nome = nome

        def get_nome(self) -> str:
            return self._nome
        def set_nome(self, new_nome: str) -> None:
            self._nome = new_nome

class Città:
    def __init__(self, nome : str, n_abitanti: int):
        if n_abitanti < 0:
            raise ValueError("Il numero di abitanti non può essere minore di 0.")
        self._nome = nome
        self._n_abitanti = n_abitanti
        
        def get_nome(self) -> str:
            return self._nome
        def set_nome(self, new_nome: str) -> None:
            self._nome = new_nome

        def get_n_abitanti(self) -> int:
            return self._n_abitanti
        def set_n_abitanti(self, new_n_abitanti: int) -> None:
            self._n_abitanti = new_n_abitanti

class Compagnia:
    def __init__(self, nome : str, fondazione : date):
        if fondazione < 1900:
            raise ValueError("La compagnia non può essere stata fondata prima del 1900.")
        self._nome = nome
        self._fondazione = fondazione

        def get_nome(self) -> str:
            return self._nome
        def set_nome(self, new_nome: str) -> None:
            self._nome = new_nome

        def get_fondazione(self) -> date:
            return self._fondazione
        def set_fondazione(self, new_fondazione: date) -> None:
            self._fondazione = new_fondazione

class Aeroporto:
    def __init__(self, nome : str ):
        self._nome = nome

        def get_nome(self) -> str:
            return self._nome
        def set_nome(self, new_nome: str) -> None:
            self._nome = new_nome

class Volo:
    def __init__(self, codice : str, durata_minuti : datetime):
        if durata_minuti < 0:
            raise ValueError("La durata del volo non può essere negativa")
        self._codice = codice
        self._durata_minuti = durata_minuti

        def get_codice(self) -> str:
            return self._codice
        def set_codice(self, new_codice: str) -> None:
            self._codice = new_codice

        def get_durata_minuti(self) -> datetime:
            return self._durata_minuti
        def set_durata_minuti(self, new_durata_minuti: datetime) -> None:
            self._durata_minuti = new_durata_minuti