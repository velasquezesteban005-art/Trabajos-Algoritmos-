import time


def binaria(vector, elemento):
    inicio = 0
    fin = len(vector) - 1
    pasos = 0

    while inicio <= fin:
        pasos += 1

        medio = (inicio + fin) // 2

        if vector[medio] == elemento:
            print("Cantidad de pasos:", pasos)
            return medio

        elif vector[medio] < elemento:
            inicio = medio + 1

        else:
            fin = medio - 1

    print("Cantidad de pasos:", pasos)
    return -1


def secuencial(vector, elemento):
    pasos = 0

    for i in range(len(vector)):
        pasos += 1

        if vector[i] == elemento:
            print("Cantidad de pasos:", pasos)
            return i

    print("Cantidad de pasos:", pasos)
    return -1



vector = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]

elemento = 18

print("Busqueda binaria")

inicio = time.perf_counter()

resultado = binaria(vector, elemento)

fin = time.perf_counter()


print("elemento", elemento, "indice en el que se encuentra:", resultado)


print("Busqueda secuencial")

inicio = time.perf_counter()

resultado = secuencial(vector, elemento)

fin = time.perf_counter()

print("elemento", elemento, "indice en el que se encuentra:", resultado)