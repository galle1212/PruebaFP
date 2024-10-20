'''
Created on 10 oct 2024

@author: guilo
'''
import math
from typing import Callable

#Funcion 1
def producto(n:int,k:int)->float:
    if n > k:
        r:float = 1
        for i in range(0,k+1):
            r:float = (n-i+1)*r
        return r
    else:
        print("El número n debe ser mayor o igual que k")


#Funcion 2
def producto_secuencia(a1:float,r:float,k:int)->float:
    lista:list[float] = list()
    for n in range(1,k+1):
        an:float = a1*r**(n-1)
        lista.append(an)
    r:float = 1
    for e in lista:
        r = e*r
    return r


#Funcion 3
def numero_combinatorio(n:int,k:int)->int:
    if n >= k:
        return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    else:
        print("El número n debe ser mayor o igual que k")


#Funcion 4
def numeroS(n:int,k:int)->float:
    if n >= k:
        fraccion:float = 1/math.factorial(k)
        suma:float = 0
        for i in range(0,k):
            n:float = ((-1)**i)*numero_combinatorio(k+1,i+1)*(k-i)**n
            suma:float = suma+n
        return fraccion*suma
    
    
#Funcion 5
def metodo_newton(f:Callable[[float],float],f_derivada:Callable[[float],float],a:float,epsilon:float)->float:
    xn:float = a
    while True:
        if abs(f(xn)) <= epsilon:
            return xn
        xn = xn-f(xn)/f_derivada(xn)
    

if __name__ == '__main__':

#Test de la funcion 1
    print(producto(4,2))
#Test de la funcion 2
    print(producto_secuencia(3,5,2))
#Test de la funcion 3
    print(numero_combinatorio(4,2))
#Test de la funcion 4
    print(numeroS(4,2))
#Test de la funcion 5
    f=lambda x:2*x**2
    f_derivada=lambda x:4*x
    print(metodo_newton(f,f_derivada,3,0.001))
    
    