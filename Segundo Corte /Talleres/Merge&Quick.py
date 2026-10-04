import time

comp_merge = 0
inter_merge = 0

def merge_sort_rec(lista):
    global comp_merge, inter_merge
    
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort_rec(lista[:medio])
    derecha = merge_sort_rec(lista[medio:])

    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        comp_merge += 1
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
        inter_merge += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def ejecutar_merge_sort(datos):
    global comp_merge, inter_merge
    comp_merge = 0
    inter_merge = 0
    
    inicio = time.perf_counter()
    lista_ordenada = merge_sort_rec(list(datos))
    fin = time.perf_counter()
    
    return lista_ordenada, comp_merge, inter_merge, (fin - inicio)



comp_quick = 0
inter_quick = 0

def particion_hoare(lista, bajo, alto):
    global comp_quick, inter_quick
    pivote = lista[bajo]  # Tomamos el primer elemento como pivote
    i = bajo - 1
    j = alto + 1

    while True:
        while True:
            i += 1
            comp_quick += 1
            if lista[i] >= pivote:
                break

        while True:
            j -= 1
            comp_quick += 1
            if lista[j] <= pivote:
                break

        if i >= j:
            return j

        lista[i], lista[j] = lista[j], lista[i]
        inter_quick += 1

def quicksort_rec(lista, bajo, alto):
    if bajo < alto:
        p = particion_hoare(lista, bajo, alto)
        quicksort_rec(lista, bajo, p)
        quicksort_rec(lista, p + 1, alto)

def ejecutar_quicksort_inplace(datos):
    global comp_quick, inter_quick
    comp_quick = 0
    inter_quick = 0
    lista = list(datos)
    
    inicio = time.perf_counter()
    quicksort_rec(lista, 0, len(lista) - 1)
    fin = time.perf_counter()
    
    return lista, comp_quick, inter_quick, (fin - inicio)

datos = [38, 27, 43, 3, 9, 82, 10]


lista_ordenada_merge, comparaciones_merge, intercambios_merge, tiempo_merge = ejecutar_merge_sort(datos)


lista_ordenada_quick, comparaciones_quick, intercambios_quick, tiempo_quick = ejecutar_quicksort_inplace(datos)


print("Merge Sort:", lista_ordenada_merge)
print("Comparaciones:", comparaciones_merge, "| Intercambios:", intercambios_merge, "| Tiempo:", tiempo_merge)

print("\nQuicksort:", lista_ordenada_quick)
print("Comparaciones:", comparaciones_quick, "| Intercambios:", intercambios_quick, "| Tiempo:", tiempo_quick)

 #Experimento del peor caso con datos ya ordenados (N = 8)
datos_ordenados = [1, 2, 3, 4, 5, 6, 7, 8]

_, comparaciones_peor_caso, intercambios_peor_caso, tiempo_peor_caso = ejecutar_quicksort_inplace(datos_ordenados)

print("\nQuicksort en peor caso (lista ya ordenada):")
print("Comparaciones:", comparaciones_peor_caso, "| Intercambios:", intercambios_peor_caso, "| Tiempo:", tiempo_peor_caso)