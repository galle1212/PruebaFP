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


class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []  # Lista de elementos
        self._priorities: List[P] = []  # Lista de prioridades asociadas
        # Inicializa dos listas vacías, una para los elementos y otra para sus prioridades
        
    @property
    def size(self) -> int:
        return len(self._elements)
        """
        Devuelve el número de elementos en la cola.
        :return: Int
        """
        
    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0
        """
        Verifica si la cola está vacía.
        :return: Boolean
        """
        
    @property
    def elements(self) -> List[E]:
        return self._elements.copy()
        """
        Devuelve una copia de la lista de elementos de mayor a menor prioridad
        :return: List
        """

    def add(self, e: E, priority: P) -> None:
        index = self._index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)
        """
        Agrega un elemento y sus prioridades a la cola.
        :param e: Elemento a agregar
        :param priority: Prioridad del elemento
        """
        
    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for e, priority in ls:
            self.add(e, priority)
        """
        Agrega todos los elementos y sus prioridades a la cola.
        :param ls: Lista de tuplas (elemento, prioridad)
        """

    def remove(self) -> E:
        assert len(self._elements) > 0, "El agregado está vacío"
        return self._elements.pop(0), self._priorities.pop(0)
        """
        Elimina el primer elemento de la cola. El primer elemento es el de mayor prioridad.
        :return: Elemento eliminado
        :raise IndexError: Si la cola está vacía
        """
        
    def remove_all(self) -> list[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements        
        
    def _index_order(self, priority: P) -> int:
        for i, existing_priority in enumerate(self._priorities):
            if priority < existing_priority:  # Menor valor representa mayor prioridad
                return i
        return len(self._priorities)

    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            index = self._elements.index(e)
            current_priority = self._priorities[index]
            if new_priority < current_priority:  # Verifica si la nueva prioridad es menor
                # Remover y volver a insertar el elemento con la nueva prioridad
                self._elements.pop(index)
                self._priorities.pop(index)
                self.add(e, new_priority)
        """
        Reduce la prioridad del elemento en la cola. El elemento debe estar en la cola, y la nueva prioridad debe ser menor
        :param e: Elemento a reducir prioridad.
        :param new_priority: Prioridad nueva para el elemento
        """
        
    def __str__(self) -> str:
        elementos = (f"({repr(el)}, {pr})" for el, pr in zip(self._elements, self._priorities))
        elementos_str = ", ".join(elementos)
        return f"ColaPrioridad[{elementos_str}]"





if __name__ == '__main__':
    pass