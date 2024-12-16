'''
Created on 28 nov 2024

@author: guilo
'''

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict
from datetime import date, datetime
from entrega3.grafos.recorridos import *
from entrega3.grafos.grafo import *

@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        return Usuario(dni,nombre,apellidos,fecha_nacimiento)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos} DNI: {self.dni}, Fecha de nacimiento: {self.fecha_nacimiento}"


@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0 # Contador de relaciones. Servirá para asignar identificadores únicos a las relaciones.
    
    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        Relacion.__n += 1
        return Relacion(Relacion.__n, interacciones, dias_activa)
    
    def __str__(self) -> str:
        return f"Relacion {self.id}: {self.interacciones} interacciones, {self.dias_activa} dias activa"


class Red_social(Grafo[Usuario, Relacion]):
    """
    Representa una red social basada en el grafo genérico.
    """
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        '''
        usuarios_dni: Diccionario que asocia un DNI de usuario con un objeto Usuario.
        Va a ser útil en la lectura del fichero de relaciones para poder acceder a los usuarios
        '''
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> Red_social:
        return Red_social(es_dirigido)
        """
        Método de factoría para crear una nueva Red Social.
        
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> Red_social:
        """
        Método de factoría para crear una Red Social desde archivos de usuarios y relaciones.
        
        :param f1: Archivo de usuarios.
        :param f2: Archivo de relaciones.
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        red_social = Red_social(es_dirigido)
    
        # Lectura del fichero de usuarios:
        with open(f1,"r") as usu:
            for linea in usu:
                dni, nombre, apellidos, fecha_nacimiento = linea.strip().split(",")
                usuario = Usuario(dni=dni, nombre=nombre, apellidos=apellidos, fecha_nacimiento=date.fromisoformat(fecha_nacimiento))
                red_social.usuarios_dni[dni] = usuario
                red_social.add_vertex(usuario)
                
        # Lectura del fichero de relaciones:
        with open(f2,"r") as rel:
            for linea in rel:
                dni_origen, dni_destino, interacciones, dias_activa = linea.strip().split(",")
                usuario_origen = red_social.usuarios_dni[dni_origen]
                usuario_destino = red_social.usuarios_dni[dni_destino]
                relacion = Relacion.of(int(interacciones), int(dias_activa))
                red_social.add_edge(usuario_origen, usuario_destino, relacion)
    
        return red_social
    
    
    
if __name__ == '__main__':
    raiz = '../../../' # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse(raiz+'resources/usuarios.txt', raiz+'resources/relaciones.txt', es_dirigido=False)

    # Vamos a representar el grafo completo de la red social
    rrss.draw("Red Social", lambda_vertice=lambda v: f"{v.nombre} {v.apellidos}", lambda_arista=lambda e: e.id)
    rrss.draw()
    
    camino = bfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'])
    print(f"El camino más corto desde 25143909I hasta 87345530M es: {camino}")    
    g_camino = rrss.subgraph(camino)
    
    g_camino.draw("Caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: e.id)
    
    