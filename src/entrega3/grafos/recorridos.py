'''
Created on 28 nov 2024

@author: guilo

-------------
Pseudocódigo:
-------------

función bfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una cola vacía
    agregar inicio a la cola
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la cola no esté vacía:
        tomar el elemento que está al frente de la cola y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo:
                si vecino no está en visitados:
                    agregar vecino a la cola
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)

-------------------------------------------------------------
función dfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una pila vacía
    agregar inicio a la pila
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la pila no esté vacía:
        tomar el elemento más reciente agregado a la pila y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo, en orden inverso:
                si vecino no está en visitados:
                    agregar vecino a la pila
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)
-------------------------------------------------------------------------

función reconstruir_camino(predecesores, destino):
    crear una lista vacía llamada camino
    establecer vértice_actual como destino

    mientras vértice_actual no sea nulo:
        agregar vértice_actual al inicio de la lista camino
        cambiar vértice_actual al predecesor de dicho vértice_actual usando el diccionario predecesores

    devolver camino

'''
from typing import TypeVar, List, Dict, Set, Optional

from entrega3.grafos.grafo import Grafo
from entrega2.tipos.Cola import Cola
from entrega2.tipos.Pila import Pila 


V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    visitados: Set[V] = set()
    cola = Cola[V].of()
    cola.add(inicio)
    predecesores: Dict[V,Optional[V]] = {inicio: None}
    
    while not cola.is_empty:
        vertice = cola.remove()
        
        if vertice == destino:
            break
        
        if vertice not in visitados:
            visitados.add(vertice)
            
            for vecino in grafo.successors(vertice):  
                if vecino not in visitados:
                    cola.add(vecino)
                    if vecino not in predecesores:
                        predecesores[vecino] = vertice

    return reconstruir_camino(predecesores, destino)
    """
    Realiza un recorrido en anchura (BFS) desde un vértice inicial hasta un vértice destino usando una Cola.
    
    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino más corto desde inicio a destino, o [] si no hay camino.
    """
    

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    visitados:set[V] = set()
    pila = Pila.of()
    pila.add(inicio)
    predecesores:Dict[V, Optional[V]] = {inicio:None}
    
    while not pila.is_empty:
        vertice = pila.remove()
        
        if vertice == destino:
            break
        
        if vertice not in visitados:
            visitados.add(vertice)
            
            for vecino in reversed(sorted(grafo.successors(vertice))):  
                if vecino not in visitados:
                    pila.add(vecino)
                    predecesores[vecino] = vertice
                    
    return reconstruir_camino(predecesores, destino)
    """
    Realiza un recorrido en profundidad (DFS) desde un vértice inicial hasta un vértice destino usando una Pila.
    
    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino más corto desde inicio a destino, o [] si no hay camino.
    """
    

def reconstruir_camino(predecesores: Dict[V,Optional[V]], destino: V) -> List[V]:
    if destino not in predecesores:
        return []
    
    camino:List[V] = list()
    vertice_actual = destino
    
    while vertice_actual is not None:
        camino.insert(0, vertice_actual)
        vertice_actual = predecesores.get(vertice_actual)
        
    # Si el camino no contiene el inicio, no es válido (no hay conexión)
    if len(camino) == 1 and predecesores[destino] is None:
        return []
    
    return camino
    """
    Reconstruye el camino desde el origen hasta el destino usando el diccionario de predecesores.
    
    :param predecesores: Diccionario que mapea cada vértice a su predecesor.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino desde el origen hasta el destino.
    """


if __name__ == '__main__':
    # Crear un grafo dirigido
    grafo = Grafo.of(es_dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_vertex("D")
    grafo.add_edge("A", "B", 5)
    grafo.add_edge("B", "C", 3)
    grafo.add_edge("A", "D", 3)
    grafo.add_edge("D", "C", 2)
    grafo.add_edge("B", "D", 3)


    print(grafo)
    # Dibujar el grafo
    grafo.draw(titulo="Mi Grafo Dirigido")
    
    caminodfs = dfs(grafo,"A","C")
    print(caminodfs)

    caminobfs = bfs(grafo,"A","C")
    print(caminobfs)
