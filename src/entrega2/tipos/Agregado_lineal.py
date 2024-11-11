'''
Created on 31 oct 2024

@author: guilo
'''

from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')

class Agregado_lineal(ABC, Generic[E]):
    """
    Clase base para los objetos agregados lineales.
    """

    def __init__(self):
        # Inicializa una lista vacía para almacenar elementos
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)
        """
        Devuelve el número de elementos en la colección.
        :return: Int
        """

    @property
    def is_empty(self) -> bool:
        return self.size == 0
        """
        Verifica si la colección está vacía.
        :return: Boolean
        """

    @property
    def elements(self) -> List[E]:
        return self._elements.copy()
        """
        Devuelve una copia de la lista de elementos.
        :return: List
        """
    
    @abstractmethod
    def add(self, e: E) -> None:
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")
        """
        Agrega un elemento a la colección.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)
        """
        Agrega todos los elementos de una lista a la colección.
        :param ls: Lista a agregar
        :raise NotImplementedError: Método abstracto
        """

    def remove(self) -> E:
        if self.is_empty:
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)
        """
        Elimina el primer elemento de la colección.
        :return: Elemento eliminado
        :raise IndexError: Si la colección está vacía
        """

    def remove_all(self) -> List[E]:
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements
        """
        Elimina todos los elementos de la colección.
        :return: Lista eliminada
        """






if __name__=="__main__":
    pass
    