'''
Created on 31 oct 2024

@author: guilo
'''

from entrega2.tipos.Pila import *

def test_pila():
    pila = Pila.of()
    
    # Prueba de añadir elementos en orden LIFO
    pila.add("Elemento 1")
    pila.add("Elemento 2")
    pila.add("Elemento 3")
    assert pila._elements == ["Elemento 3", "Elemento 2", "Elemento 1"], "Test 1 falló"
    print("Test 1 (orden de inserción LIFO): PASSED")

    # Prueba de eliminación LIFO (Last In, First Out)
    assert pila.remove() == "Elemento 3" and pila._elements == ["Elemento 2", "Elemento 1"], "Test 2 falló"
    print("Test 2 (eliminación LIFO): PASSED")

    # Verificar si la pila no está vacía
    assert not pila.is_empty, "Test 3 falló"
    print("Test 3 (verificación de pila no vacía): PASSED")

    # Prueba de eliminar todos los elementos
    assert pila.remove_all() == ["Elemento 2", "Elemento 1"] and pila.is_empty, "Test 4 falló"
    print("Test 4 (eliminar todos los elementos): PASSED")

    print("Todas las pruebas pasaron exitosamente.")

# Llamar a la función de prueba

if __name__ == '__main__':
    test_pila()