'''
Created on 9 dic 2024

@author: guilo
'''
from entrega3.grafos.grafo import *


def test_grafo():

    # GRAFO DIRIGIDO
    print("Creamos un grafo dirigido:")
    
    grafo_dirigido:Grafo[V,E] = Grafo.of(es_dirigido=True)
    assert grafo_dirigido.es_dirigido is True

    # Agregamos los vértices y las aristas
    grafo_dirigido.add_vertex("A")
    grafo_dirigido.add_vertex("B")
    grafo_dirigido.add_vertex("C")
    grafo_dirigido.add_edge("A", "B", 5)
    grafo_dirigido.add_edge("B", "C", 3)

    assert grafo_dirigido.vertices() == {"A", "B", "C"}
    assert grafo_dirigido.edge_exists("A", "B") is True
    assert grafo_dirigido.edge_weight("A", "B") == 5
    assert grafo_dirigido.edge_weight("B", "A") is None  # Las aristas solo tienen una direccion
    
    print(grafo_dirigido)
    
    # Representamos el grafo dirigido
    grafo_dirigido.draw(titulo="Mi Grafo Dirigido")

    
    # GRAFO NO DIRIGIDO
    print("Creamos otro grafo no dirigido:")
    
    grafo_no_dirigido:Grafo[V,E] = Grafo.of(es_dirigido=False)
    assert grafo_dirigido.es_dirigido is True
    
    # Agregamos los vértices y las aristas
    grafo_no_dirigido.add_vertex("X")
    grafo_no_dirigido.add_vertex("Y")
    grafo_no_dirigido.add_vertex("Z")
    grafo_no_dirigido.add_edge("X", "Y", 7)
    grafo_no_dirigido.add_edge("Y", "Z", 3)

    assert grafo_no_dirigido.edge_exists("X", "Y") is True
    assert grafo_no_dirigido.edge_exists("Y", "X") is True  # Las aristas son bidireccionales
    
    print(grafo_no_dirigido)
    
    # Representamos el grafo no dirigido
    grafo_no_dirigido.draw(titulo="Mi Grafo No Dirigido")

    
    # Comprobamos que funcionan los sucesores y predecesores 
    assert grafo_dirigido.successors("A") == {"B"}
    assert grafo_dirigido.predecessors("B") == {"A"}

    assert grafo_no_dirigido.successors("X") == {"Y"}
    assert grafo_no_dirigido.predecessors("Y") == {"X","Z"}
    
    
    # Hacemos un subgrafo
    print("Hacemos un subgrafo del grafo dirigido:")
    subgrafo_dirigido:Grafo[V,E] = grafo_dirigido.subgraph({"A", "B"})
    assert subgrafo_dirigido.vertices() == {"A", "B"}
    assert subgrafo_dirigido.edge_exists("A", "B") is True
    assert subgrafo_dirigido.edge_exists("B", "C") is False

    print(subgrafo_dirigido)
    subgrafo_dirigido.draw(titulo="Mi Subgrafo")


    # Hacemmos un Grafo inverso
    print("Invertimos el grafo dirigido:")
    grafo_inverso:Grafo[V,E] = grafo_dirigido.inverse_graph()
    assert grafo_inverso.edge_exists("B", "A") is True
    assert grafo_inverso.edge_weight("B", "A") == 5
    assert grafo_inverso.edge_exists("C", "B") is True

    print(grafo_inverso)


if __name__ == "__main__":
    test_grafo()

