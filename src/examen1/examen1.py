'''
Created on 24 oct 2024

@author: guilo
'''

import math
from typing import List,Tuple
import csv
from collections import Counter

#DEFINICION DE FUNCIONES
#Funcion 1

def P2(n:int, k:int, i:int=1)->int:
    assert n>=0 and k>=0 and i>=0, "los parametros deben ser positivos"
    assert i<k+1, "i debe ser menor que k+1"
    assert n>=k, "n debe ser mayor o igual que k"

    prod:int=1
    for i in range(i,k-1):
        e:int = n-i+1
        prod:int = e*prod
    return prod


#Funcion 2

def C2(n:int,k:int)->int:
    assert n>=0 and k>=0, "Los parametros deben ser positivos"
    assert n>k, "n debe ser mayor que k"
    
    k=k+1
    
    num_comb:int = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return int(num_comb)


#Funcion 3

def S2(n:int,k:int)->float:
    assert n>=0 and k>=0, "Los parametros deben ser positivos"
    assert n>k, "n debe ser mayor que k"

    fraccion:float = math.factorial(k)/(n*math.factorial(k+2))
    sumatorio:float = 0
    for i in range(0,k):
        n:float = ((-1)**i)*math.comb(k,i)*(k-i)**(n+1)
        sumatorio:float = sumatorio+n
    return fraccion*sumatorio


#Funcion 4

def palabrasMasComunes(fichero:str,n:int=5)->List[Tuple[str,int]]:
    assert n>1, "n debe ser mayor que 1"
    
    fichero=fichero.lower()
    
    with open(fichero,encoding="UTF-8") as f:
        lector=csv.reader(f,delimiter=" ")
        contador=Counter()
        for linea in lector:
            e = Counter(linea)
            contador.update(e)

    return contador.most_common(n)

#TESTEOS DE FUNCIONES

#Test funcion 1

def test_P2():
    print("Pruebas para P2:")
    
    # Caso válido
    print(P2(8, 5, 2))
    
    # Caso no válido: parámetros negativos
    try:
        print(P2(-1, -5, -2))
    except AssertionError as e:
        print(f"Error:",e)

    # Caso no válido: i >= k+1
    try:
        print(P2(3, 4, 6))
    except AssertionError as e:
        print(f"Error:",e)
    

    # Caso no válido: n < k
    try:
        print(P2(3, 6, 5))
    except AssertionError as e:
        print(f"Error:",e)


#Test funcion 2

def test_C2():
    print("Pruebas para C2:")
    
    # Caso válido
    print(C2(10, 2))

    # Caso no válido: parámetros negativos
    try:
        print(C2(-1, -2))
    except AssertionError as e:
        print(f"Error:",e)

    # Caso no válido: n <= k
    try:
        print(C2(2, 5))
    except AssertionError as e:
        print(f"Error:",e)
    
    
#Test funcion 3

def test_S2():
    print("Pruebas para S2:")
    
    # Caso válido
    print(S2(4, 2))

    # Caso no válido: parámetros negativos
    try:
        print(S2(-4, -2))
    except AssertionError as e:
        print(f"Error:",e)

    # Caso no inválido: n < k
    try:
        print(S2(2, 4))
    except AssertionError as e:
        print(f"Error:",e)


#Test funcion 4

def test_palabrasMasComunes():
    print("Pruebas para palabrasMasComunes:")
    
    # Caso válido
    print(palabrasMasComunes('../../resources/archivo_palabras.txt', 3))  # Esperado: lista con las palabras menos comunes

    # Caso no válido: n <= 1
    try:
        print(palabrasMasComunes('../../resources/archivo_palabras.txt', 0))  # Esperado: AssertionError
    except AssertionError as e:
        print(f"Error:",e)



if __name__ == '__main__':

    test_P2()
    print()
    test_C2()
    print()
    test_S2()
    print()
    test_palabrasMasComunes()
    