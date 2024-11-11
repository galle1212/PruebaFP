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


class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    
    def __init__(self, order: Callable[[E], R]):
        # Inicializa la colección con una función de ordenación
        super().__init__()
        self._order = order

    @classmethod
    def of(cls, order: Callable[[E], R]) -> "Lista_ordenada[E, R]":
        return cls(order)
        """
        Crea una instancia de la clase lista ordenada.
        :param order: Función de ordenación
        :return: Instancia de Lista_ordenada
        """      

    def __index_order(self, e: E) -> int:
        key = self._order(e)
        for i, existing_element in enumerate(self._elements):
            if key < self._order(existing_element):
                return i
        return len(self._elements)
        """
        Busca el índice correspondiente a un elemento en la colección.
        :param e: Elemento a buscar
        :return: int
        """

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)
        """
        Inserta un elemento en el lugar correspondiente
        :param e: Elemento a agregar
        """
        
    def __str__(self) -> str:
        elementos = (repr(el) for el in self._elements)
        elementos_str = ",".join(elementos)
        return f"ListaOrdenada({elementos_str})"




if __name__ == '__main__':
    pass