'''
Created on 31 oct 2024

@author: guilo
'''

from entrega2.tipos.Agregado_lineal import *
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')

class Pila(Agregado_lineal[E]):
    
    def __init__(self):
        super().__init__()
    
    @classmethod
    def of(cls) -> "Pila[E]":
        return cls()
    
    
    def add(self, e: E) -> None:
        self._elements.insert(0, e)  # Se inserta al principio de la lista
    

    def __str__(self) -> str:
        elementos = (repr(el) for el in self._elements)
        elementos_str = ",".join(elementos)
        return f"Pila({elementos_str})"





if __name__ == '__main__':
    pass