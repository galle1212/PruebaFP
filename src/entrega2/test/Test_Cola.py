'''
Created on 31 oct 2024

@author: guilo
'''

from entrega2.tipos.Cola import *


def test_cola():
    cola = Cola.of()
    
    # Prueba de añadir elementos y orden FIFO
    cola.add("Elemento 1")
    cola.add("Elemento 2")
    cola.add("Elemento 3")
    assert cola._elements == ["Elemento 1", "Elemento 2", "Elemento 3"], "Test 1 falló"
    print("Test 1 (orden de inserción FIFO): PASSED")

    # Prueba de eliminación FIFO
    assert cola.remove() == "Elemento 1" and cola._elements == ["Elemento 2", "Elemento 3"], "Test 2 falló"
    print("Test 2 (eliminación FIFO): PASSED")

    # Verificar si no está vacía
    assert not cola.is_empty, "Test 3 falló"
    print("Test 3 (verificación de cola no vacía): PASSED")

    # Prueba de eliminar todos los elementos
    assert cola.remove_all() == ["Elemento 2", "Elemento 3"] and cola.is_empty, "Test 4 falló"
    print("Test 4 (eliminar todos los elementos): PASSED")

    print("Todas las pruebas pasaron exitosamente.")


if __name__ == '__main__':
    test_cola()