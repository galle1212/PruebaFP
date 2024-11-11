'''
Created on 31 oct 2024

@author: guilo
'''

from entrega2.tipos.Lista_ordenada_sin_repeticion import *



def test_lista_ordenada_sin_repeticion():
    # Crear una instancia de ListaOrdenadaSinRepeticion con criterio de ordenación
    lista = Lista_ordenada_sin_repeticion.of(lambda x: x)

    # Prueba de añadir elementos y mantener el orden sin duplicados
    lista.add(10)
    lista.add(5)
    lista.add(20)
    lista.add(15)
    assert lista._elements == [5, 10, 15, 20], "Test 1 falló"
    print("Test 1 (ordenación sin duplicados): PASSED")

    # Intentar añadir un elemento duplicado
    lista.add(10)
    assert lista._elements == [5, 10, 15, 20], "Test 2 falló"
    print("Test 2 (evitar duplicados): PASSED")

    # Prueba de añadir un elemento en una posición intermedia
    lista.add(12)
    assert lista._elements == [5, 10, 12, 15, 20], "Test 3 falló"
    print("Test 3 (inserción en posición intermedia sin duplicados): PASSED")

    # Verificar si la lista no está vacía
    assert not lista.is_empty, "Test 4 falló"
    print("Test 4 (verificación de lista no vacía): PASSED")

    # Prueba de eliminar el primer elemento
    assert lista.remove() == 5 and lista._elements == [10, 12, 15, 20], "Test 5 falló"
    print("Test 5 (eliminar primer elemento): PASSED")

    # Prueba de eliminar todos los elementos
    assert lista.remove_all() == [10, 12, 15, 20] and lista.is_empty, "Test 6 falló"
    print("Test 6 (eliminar todos los elementos): PASSED")

    print("Todas las pruebas pasaron exitosamente.")



if __name__ == '__main__':
    test_lista_ordenada_sin_repeticion()
