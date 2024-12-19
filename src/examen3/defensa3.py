'''
Created on 19 dic 2024

@author: guilo
'''
from dataclasses import dataclass
from typing import List, Tuple, TypeVar, Generic, Dict, Set, Optional, Callable
from entrega3.grafos.grafo import Grafo
from entrega3.grafos.recorridos import *
import matplotlib.pyplot as plt
import networkx as nx

@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> 'Gen':
        if num_mutaciones < 0:
            raise ValueError("El numero de mutaciones debe ser mayor o igual a cero.")
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(linea: str) -> 'Gen':
        partes = linea.strip().split(",")

        nombre = str(partes[0])
        tipo = str(partes[1])
        num_mutaciones = int(partes[2])
        loc_cromosoma = str(partes[3])
        
        return Gen.of(nombre, tipo, num_mutaciones, loc_cromosoma)



@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> 'RelacionGenAGen':
        if not (-1 <= conexion <= 1):
            raise ValueError("El valor de conexión debe estar entre -1 y 1, ambos inclusive.")
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(linea: str) -> 'RelacionGenAGen':
        partes = linea.strip().split(",")

        nombre_gen1 = str(partes[0])
        nombre_gen2 = str(partes[1])
        conexion = float(partes[2])
        
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, conexion)

    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.conexion < 0.75




class RedGenica(Grafo[Gen, RelacionGenAGen]):
    """
    Representa una red génica basada en un grafo donde los vértices son genes
    y las aristas son relaciones entre genes.
    """
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}
            
    @staticmethod
    def of(es_dirigido: bool = False) -> 'RedGenica':
        """
        Método de factoría para crear una nueva Red Génica.
        
        :param es_dirigido: Indica si la red génica es dirigida (True) o no dirigida (False).
        :return: Nueva red génica.
        """
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> 'RedGenica':
        """
        Método de factoría para crear una Red Génica desde archivos de genes y relaciones.
        
        :param f1: Archivo de genes.
        :param f2: Archivo de relaciones entre genes.
        :param es_dirigido: Indica si la red génica es dirigida (True) o no dirigida (False).
        :return: Nueva red génica.
        """
        # Crear una nueva red génica
        red_genica = RedGenica.of(es_dirigido)

        # Leer y agregar genes desde el archivo f1
        with open(f1, 'r') as archivo_genes:
            for linea in archivo_genes:
                gen = Gen.parse(linea)
                red_genica.add_vertex(gen)
                red_genica.genes_por_nombre[gen.nombre] = gen

        # Leer y agregar relaciones entre genes desde el archivo f2
        with open(f2, 'r') as archivo_relaciones:
            for linea in archivo_relaciones:
                relacion = RelacionGenAGen.parse(linea)
                gen1 = red_genica.genes_por_nombre.get(relacion.nombre_gen1)
                gen2 = red_genica.genes_por_nombre.get(relacion.nombre_gen2)

                if gen1 and gen2:
                    red_genica.add_edge(gen1, gen2, relacion)
        
        return red_genica

    def __str__(self) -> str:
        """
        Representación textual de la red génica.
        
        Muestra todos los genes y sus relaciones.
        """
        lines = []
        for gen in self.genes_por_nombre.values():
            relaciones = ", ".join(
                f"{relacion.nombre_gen2} ({relacion.conexion})" 
                for relacion in self.adyacencias.get(gen, {}).values()
            )
            lines.append(f"{gen.nombre} -> {relaciones}")
        return "\n".join(lines)



#TEST
def test_red_genica():
    # 1: Red Génica no dirigida a partir de los ficheros genes.txt y red_genes.txt
    red_genica = RedGenica.parse('../../resources/genes.txt', '../../resources/red_genes.txt', es_dirigido=False)
    print(red_genica)
    # 2: Recorrido en profundidad desde el gen KRAS hasta el gen PIK3CA
    camino = dfs(red_genica, 'KRAS', 'PIK3CA')
    
    print("Camino encontrado desde KRAS hasta PIK3CA en DFS :")
    print(camino)


    # 3:Subgrafo a partir de los vértices del camino
    subgrafo = red_genica.subgraph(camino)

    # Funciones lambda para personalizar la representación de los vértices y las aristas
    lambda_vertice = lambda gen: gen.nombre  # Mostrar el nombre del gen en cada vértice
    lambda_arista = lambda relacion: f"{relacion.conexion:.2f}"  # Mostrar la conexión de la relación entre genes

    # Dibujar el subgrafo
    subgrafo.draw(titulo="Subgrafo entre KRAS y PIK3CA", lambda_vertice=lambda_vertice, lambda_arista=lambda_arista)




if __name__ == "__main__":
    # Comprobamos el metodo parse de la clase Gen
    ejemplo_linea = "TP53,supresor tumoral,256,17p13.1"
    gen = Gen.parse(ejemplo_linea)
    print(gen)
    
    # Comprobamos el metodo parse de la clase RelacionGenAGen
    ejemplo_linea = "TP53,EGFR,0.8"
    relacion = RelacionGenAGen.parse(ejemplo_linea)
    print(relacion)
    print("Coexpresados:", relacion.coexpresados)
    print("Antiexpresados:", relacion.antiexpresados)
    
    test_red_genica()
    
    
    