'''
Created on 21 nov 2024

@author: guilo
'''
from entrega2.tipos.Agregado_lineal import *
from typing import List, TypeVar, Generic, Callable, Tuple


E = TypeVar('E')

class ColaConLimite(Agregado_lineal[E], Generic[E]):
    
    def __init__(self, capacidad: int):
        super().__init__()
        self.capacidad = capacidad


    @staticmethod
    def of(capacidad: int) -> "ColaConLimite[E]":
        return ColaConLimite(capacidad)


    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    def is_full(self) -> bool:
        return len(self._elements) >= self.capacidad


    def __str__(self) -> str:
        elementos = ', '.join(map(str, self._elements))
        return f"ColaConLimite({elementos})"



#TESTS

#Test para ColaConLimite
def test_cola_con_limite():
    print("Iniciando pruebas para ColaConLimite...")

    # Prueba: Creación con capacidad
    cola = ColaConLimite.of(3)
    assert cola.is_empty, "La cola debe estar vacía al inicio."
    assert not cola.is_full(), "La cola no debe estar llena al inicio."

    # Prueba: Agregar elementos dentro del límite
    cola.add(1)
    cola.add(2)
    cola.add(3)
    assert cola.size == 3, "La cola debe tener tres elementos."
    assert cola.is_full(), "La cola debe estar llena con tres elementos."

    # Prueba: Excepción al intentar agregar más elementos de los permitidos
    try:
        cola.add(4)
        assert False, "Agregar un elemento adicional debe lanzar OverflowError."
    except OverflowError as e:
        assert str(e) == "La cola está llena. No se pueden agregar más elementos."

    # Prueba: Remover elementos
    assert cola.remove() == 1, "El primer elemento eliminado debe ser 1."
    assert cola.remove() == 2, "El siguiente elemento eliminado debe ser 2."
    assert not cola.is_full(), "La cola ya no debe estar llena."
    assert not cola.is_empty, "La cola no debe estar vacía aún."

    # Prueba: Vaciar la cola
    assert cola.remove() == 3, "El último elemento eliminado debe ser 3."
    assert cola.is_empty, "La cola debe estar vacía después de eliminar todos los elementos."

    # Prueba: Excepción al intentar eliminar de una cola vacía
    try:
        cola.remove()
        assert False, "Remover de una cola vacía debe lanzar AssertionError."
    except AssertionError as e:
        assert str(e) == "El agregado está vacío"

    print("Pruebas para ColaConLimite completadas con éxito.")
    


#Test para Agregado_lineal
def test_agregado_lineal():
    print("Iniciando pruebas para las funcionalidades añadidas en Agregado_lineal...")

    agregado = Agregado_lineal[int]()
    agregado._elements = [1, 2, 3, 4, 5]

    # Prueba: contains
    assert agregado.contains(3), "El agregado debe contener el elemento 3."
    assert not agregado.contains(6), "El agregado no debe contener el elemento 6."

    # Prueba: find
    assert agregado.find(lambda x: x > 3) == 4, "El primer elemento mayor que 3 debe ser 4."
    assert agregado.find(lambda x: x < 0) is None, "No debe encontrarse un elemento menor que 0."

    # Prueba: filter
    assert agregado.filter(lambda x: x % 2 == 0) == [2, 4], "Los elementos pares deben ser [2, 4]."
    assert agregado.filter(lambda x: x > 10) == [], "No debe haber elementos mayores que 10."

    # Prueba: Vaciar el agregado
    agregado._elements = []
    assert agregado.is_empty, "El agregado debe estar vacío después de vaciarlo."
    assert agregado.find(lambda x: True) is None, "No debe encontrarse ningún elemento en un agregado vacío."

    # Prueba: Añadir y eliminar
    agregado._elements = [10, 20, 30]
    assert agregado.remove() == 10, "El primer elemento eliminado debe ser 10."
    agregado.add_all([40, 50])
    assert agregado._elements == [20, 30, 40, 50], "El agregado debe contener los elementos [20, 30, 40, 50]."

    print("Pruebas para AgregadoLineal completadas con éxito.")
    
    
    
if __name__ == "__main__":
    
    test_cola_con_limite()
    test_agregado_lineal()