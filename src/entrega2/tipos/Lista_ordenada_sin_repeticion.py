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


class Lista_ordenada_sin_repeticion(Agregado_lineal[E], Generic[E, R]):
    
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order
    
    @classmethod
    def of(cls, order: Callable[[E], R]) -> "Lista_ordenada_sin_repeticion[E, R]":
        return cls(order)
    
    def __index_order(self, e: E) -> int:
        key = self._order(e)
        for i, existing_element in enumerate(self._elements):
            if key < self._order(existing_element):
                return i
        return len(self._elements)
    
    def add(self, e: E) -> None:
        if e not in self._elements:
            index = self.__index_order(e)
            self._elements.insert(index, e)    
        """
        Agrega un elemento a la colección sin repetición.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        
    def __str__(self) -> str:
        elementos = (repr(el) for el in self._elements)
        elementos_str = ",".join(elementos)
        return f"ListaOrdenadaSinRepeticion({elementos_str})"





if __name__ == '__main__':
    pass