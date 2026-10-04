def temperaturas_diarias(temps):
    resultado = [0] * len(temps)
    pila = []
    for i, temp in enumerate(temps):
        while pila and temps[pila[-1]] < temp:
            indice = pila.pop()
            resultado[indice] = i - indice
        pila.append(i)
    return resultado

temperaturas_diarias([73, 74, 75, 71, 69, 72, 76, 73])
print(temperaturas_diarias([73, 74, 75, 71, 69, 72, 76, 73]))