import time
import random

def busqueda_secuencial(arr, objetivo):
    comparaciones = 0
    for i, val in enumerate(arr):
        comparaciones += 1
        if val == objetivo:
            return i, comparaciones
    return -1, comparaciones

def busqueda_binaria(arr, objetivo):
    
    izquierda, derecha = 0, len(arr) - 1
    comparaciones = 0
    while izquierda <= derecha:
        comparaciones += 1
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio, comparaciones
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, comparaciones