'''
Created on 9 dic 2024

@author: guilo
'''
from entrega3.grafos.recorridos import *


def test_recorridos():

    # GRAFO DIRIGIDO
    grafo_dirigido = Grafo.of(es_dirigido=True)
    grafo_dirigido.add_vertex("A")
    grafo_dirigido.add_vertex("B")
    grafo_dirigido.add_vertex("C")
    grafo_dirigido.add_vertex("D")
    grafo_dirigido.add_edge("A", "B", 5)
    grafo_dirigido.add_edge("B", "C", 3)
    grafo_dirigido.add_edge("A", "D", 3)
    grafo_dirigido.add_edge("D", "C", 2)
    grafo_dirigido.add_edge("B", "D", 3)

    print("Grafo dirigido de prueba:")
    print(grafo_dirigido)

    # Prueba del BFS con un grafo dirigido:
    print("Hacemos un BFS (A -> C)")
    camino_bfs_dir = bfs(grafo_dirigido, "A", "C")
    print(camino_bfs_dir)
    assert camino_bfs_dir in (["A", "B", "C"], ["A", "D", "C"]), "El BFS no encontró el camino más corto correctamente."

    # Prueba del DFS con un grafo dirigido:
    print("Hacemos un DFS (A -> C)")
    camino_dfs_dir = dfs(grafo_dirigido, "A", "C")
    print(camino_dfs_dir)
    assert camino_dfs_dir == ["A", "B", "C"], "El DFS no encontró un camino válido."


    # GRAFO NO DIRIGIDO
    grafo_no_dirigido = Grafo.of(es_dirigido=False)
    grafo_no_dirigido.add_vertex("A")
    grafo_no_dirigido.add_vertex("B")
    grafo_no_dirigido.add_vertex("C")
    grafo_no_dirigido.add_vertex("D")
    grafo_no_dirigido.add_edge("A", "B", 5)
    grafo_no_dirigido.add_edge("B", "C", 3)
    grafo_no_dirigido.add_edge("A", "D", 3)
    grafo_no_dirigido.add_edge("D", "C", 2)
    grafo_no_dirigido.add_edge("B", "D", 3)

    print("Grafo no dirigido de prueba:")
    print(grafo_no_dirigido)
    
    # Prueba del BFS con un grafo no dirigido:
    print("Hacemos un BFS (A -> C)")
    camino_bfs_nodir = bfs(grafo_no_dirigido, "A", "C")
    print(camino_bfs_nodir)
    assert camino_bfs_nodir in (["A", "B", "C"], ["A", "D", "C"]), "El BFS no encontró el camino más corto correctamente."

    # Prueba del DFS con un grafo no dirigido:
    print("Hacemos un DFS (A -> C)")
    camino_dfs_nodir = dfs(grafo_dirigido, "A", "C")
    print(camino_dfs_nodir)
    assert camino_dfs_nodir == ["A", "B", "C"], "El DFS no encontró un camino válido."


    # Probamos el caso en el que el camino no exista:
    print("Caso en el que hay un camino inexistente (C -> A):")
    camino_bfs_inexistente = bfs(grafo_dirigido, "C", "A")
    camino_dfs_inexistente = dfs(grafo_dirigido, "C", "A")
    print(f"Camino BFS de C a A: {camino_bfs_inexistente}")
    assert camino_bfs_inexistente == [], "El BFS no identificó correctamente que no hay camino."
    print(f"Camino DFS de C a A: {camino_dfs_inexistente}")
    assert camino_dfs_inexistente == [], "El DFS no identificó correctamente que no hay camino."
    

    # Probamos la reconstrucción de camino
    print("Comprobamos que se reconstruya el camino correctamente.")
    predecesores = {"C": "B", "B": "A", "A": None}
    camino_reconstruido = reconstruir_camino(predecesores, "C")
    print(f"Camino reconstruido desde A a C: {camino_reconstruido}")
    assert camino_reconstruido == ["A", "B", "C"], "La función reconstruir_camino falló."

    
    
if __name__ == '__main__':
    test_recorridos()
    
    