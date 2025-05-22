from enum import *
import re

class Indirizzo:
    def __init__(self, via: str, civico: int, cap: str) -> None:
        self._via = via
        self._civico = civico
        self._cap = self.cap_validation(cap)

    def via(self):
        return self._via
    
    def civico(self):
        return self._civico

    def cap(self):
        return self._cap

    @staticmethod
    def cap_validation(cap: str) -> str:
        pattern = r'^\d{5}$'
        if re.match(pattern, cap):
            return cap
        raise ValueError(f'CAP non valido: {cap}')

    def __hash__(self):
        return hash((self._via, self._civico, self._cap))
    
    def __eq__(self, other):
        return isinstance(other, Indirizzo) and self._via == other._via and self._civico == other._civico and self._cap == other._cap

class Stato_Ordine(StrEnum):
    in_preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

class Codice_Fiscale:
    def __init__(self, cod_fisc: str):
        self.cod_fisc = self.cod_fisc_validation(cod_fisc)

    def cod_fisc_validation(self, cod_fisc: str) -> str:
        pattern = r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$'
        cod_fisc = cod_fisc.upper()
        if re.match(pattern, cod_fisc):
            return cod_fisc
        raise ValueError(f'Codice fiscale non valido: {cod_fisc}')
    
    def __hash__(self):
        return hash(self.cod_fisc)
    
    def __eq__(self, other):
        return isinstance(other, Codice_Fiscale) and self.cod_fisc == other.cod_fisc
    
class Partita_Iva(str):
    def __new__(cls, iva: str):
        pattern = r'^\d{11}$'
        if re.match(pattern, iva):
            return str.__new__(cls, iva)
        raise ValueError(f'Partita IVA non valida: {iva}')
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        return isinstance(other, Partita_Iva) and str(self) == str(other)

class Telefono(str):
    def __new__(cls, telefono: str):
        pattern = r'^\+?\d{1,4}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$'
        if re.match(pattern, telefono):
            return str.__new__(cls, telefono)
        raise ValueError(f'Numero di telefono non valido: {telefono}')
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        return isinstance(other, Telefono) and str(self) == str(other)

class Email(str):
    def __new__(cls, email: str):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return super().__new__(cls, email)
        raise ValueError(f'Email non valida: {email}')

class Aliquota(float):
    def __new__(cls, aliquota: float):
        if 0 < aliquota <= 1:
            return super().__new__(cls, aliquota)
        raise ValueError(f'Aliquota non valida: {aliquota}')
    
    def __hash__(self):
        return hash(float(self))
    
    def __eq__(self, other):
        return isinstance(other, Aliquota) and float(self) == float(other)

if __name__ == '__main__':
    indirizzo1 = Indirizzo("Via Maurizio Quadrio", 30, "00152")
    indirizzo2 = Indirizzo("Via Maurizio Quadrio", 30, "00152")

    print(f"Indirizzo: {indirizzo1.via()}, {indirizzo1.civico()}, {indirizzo1.cap()}")

    a = Codice_Fiscale('MRCLCU04T14H501V')
    b = Codice_Fiscale('MRCLCU04T14H501V')

    print(f"Codice Fiscale: {a.cod_fisc}")

    partita_iva = Partita_Iva('12345678901')
    print(f"Partita IVA: {partita_iva}")

    telefono = Telefono('+39 327-199-4881')
    print(f"Numero di telefono: {telefono}")

    email = Email('lacumarchi@gmail.com')
    print(f"Email: {email}")

    aliquota = Aliquota(0.22)
    print(f"Aliquota: {aliquota}")