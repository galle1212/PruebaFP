'''
Created on 3 oct 2024

@author: guilo
'''
import csv

#Lecturas de ficheros
#Funcion 6

def cuenta_palabras_cad(fichero:str,sep:str,cad:str)->int:
    with open(fichero,encoding = "UTF-8") as f:
        lector = csv.reader(f,delimiter = sep)
        n:int = 0
        for linea in lector:
            for palabra in linea:
                if cad == palabra:
                    n = n+1
        return n

#Funcion 7

def lista_con_la_palabra_cad(fichero:str,cad:str)->list[str]:
    with open(fichero,encoding = "UTF-8") as f:
        lista_cad:list[str] = list()
        for linea in f:
            if cad in linea:
                lista_cad.append(linea.rstrip("\n"))
        return lista_cad

#Funcion 8

def lista_palabras_sin_repetir(fichero:str)->list[str]:
    with open(fichero,encoding = "UTF-8") as f:
        lector = csv.reader(f,delimiter = " ")
        lista:list[str] = list()
        for linea in lector:
            for palabra in linea:
                if palabra not in lista:
                    lista.append(palabra)
        return lista

#Funcion 9

def longitud_promedio_lineas(fichero:str)->float:
    with open(fichero,encoding = "UTF-8") as f:
        lector = csv.reader(f,delimiter=",")
        num_palabras:int = 0
        num_lineas:int = 0
        for linea in lector:
            num_lineas = num_lineas+1
            for _ in linea:
                num_palabras = num_palabras+1
        if num_lineas != 0:
            return num_palabras/num_lineas
        else:
            return None



if __name__ == '__main__':
#Test de la funcion 6
    print(cuenta_palabras_cad("../../resources/lin_quijote.txt"," ","de"))
#Test de la funcion 7
    print(lista_con_la_palabra_cad("../../resources/lin_quijote.txt","de"))
#Test de la funcion 8
    print(lista_palabras_sin_repetir("../../resources/archivo_palabras.txt"))
#Test de la funcion 9
    print(longitud_promedio_lineas("../../resources/palabras_random.csv"))
    print(longitud_promedio_lineas("../../resources/vacio.csv"))
    
    
    
    
    