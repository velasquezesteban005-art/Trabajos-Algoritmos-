def suma_lista(lista, i=0):
    if i == len(lista):              # caso base: lista vacía
        return 0
    return lista[i] + suma_lista(lista, i + 1)   # cabeza + suma(cola)


if __name__ == "__main__":
    v = [3, 7, 1, 9, 4]
    print("Suma:", suma_lista(v))  