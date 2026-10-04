import time
import random

comparaciones_heap = 0
intercambios_heap = 0

def hundir_nodo_minimo(lista, tamano_heap, indice_actual):
    global comparaciones_heap, intercambios_heap
    indice_menor = indice_actual
    hijo_izquierdo = 2 * indice_actual + 1
    hijo_derecho = 2 * indice_actual + 2


    if hijo_izquierdo < tamano_heap:
        comparaciones_heap += 1
        if lista[hijo_izquierdo] < lista[indice_menor]:
            indice_menor = hijo_izquierdo

    if hijo_derecho < tamano_heap:
        comparaciones_heap += 1
        if lista[hijo_derecho] < lista[indice_menor]:
            indice_menor = hijo_derecho

    if indice_menor != indice_actual:
        lista[indice_actual], lista[indice_menor] = lista[indice_menor], lista[indice_actual]
        intercambios_heap += 1
        hundir_nodo_minimo(lista, tamano_heap, indice_menor)

def ejecutar_heapsort_minimos(datos_originales):
    global comparaciones_heap, intercambios_heap
    comparaciones_heap = 0
    intercambios_heap = 0
    lista_trabajo = list(datos_originales)
    cantidad_elementos = len(lista_trabajo)

    tiempo_inicio = time.perf_counter()

    for i in range(cantidad_elementos // 2 - 1, -1, -1):
        hundir_nodo_minimo(lista_trabajo, cantidad_elementos, i)

    for i in range(cantidad_elementos - 1, 0, -1):
        lista_trabajo[0], lista_trabajo[i] = lista_trabajo[i], lista_trabajo[0]
        intercambios_heap += 1
        hundir_nodo_minimo(lista_trabajo, i, 0)
        
    tiempo_fin = time.perf_counter()
    duracion_segundos = tiempo_fin - tiempo_inicio
    
    return lista_trabajo, comparaciones_heap, intercambios_heap, duracion_segundos

def ordenamiento_insercion_subcubeta(lista_cubeta):
    comparaciones = 0
    intercambios = 0
    for i in range(1, len(lista_cubeta)):
        valor_actual = lista_cubeta[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if lista_cubeta[j] > valor_actual:
                lista_cubeta[j + 1] = lista_cubeta[j]
                intercambios += 1
                j -= 1
            else:
                break
        lista_cubeta[j + 1] = valor_actual
    return lista_cubeta, comparaciones, intercambios

def ejecutar_bucket_sort(datos_originales, cantidad_cubetas=5):
    if len(datos_originales) == 0:
        return datos_originales, 0, 0, 0
        
    lista_trabajo = list(datos_originales)
    valor_minimo, valor_maximo = min(lista_trabajo), max(lista_trabajo)
    
    if valor_minimo == valor_maximo:
        return lista_trabajo, 0, 0, 0
        
    rango_cubeta = (valor_maximo - valor_minimo) / cantidad_cubetas
    arreglo_cubetas = [[] for _ in range(cantidad_cubetas)]
    
    tiempo_inicio = time.perf_counter()
    
    for numero in lista_trabajo:
        indice_cubeta = int((numero - valor_minimo) / rango_cubeta)
        if indice_cubeta >= cantidad_cubetas:
            indice_cubeta = cantidad_cubetas - 1
        arreglo_cubetas[indice_cubeta].append(numero)
        

    resultado_final = []
    comparaciones_totales = 0
    intercambios_totales = 0
    
    for cubeta in arreglo_cubetas:
        cubeta_ordenada, comp_sub, inter_sub = ordenamiento_insercion_subcubeta(cubeta)
        resultado_final.extend(cubeta_ordenada)
        comparaciones_totales += comp_sub
        intercambios_totales += inter_sub
        
    tiempo_fin = time.perf_counter()
    duracion_segundos = tiempo_fin - tiempo_inicio
    
    return resultado_final, comparaciones_totales, intercambios_totales, duracion_segundos


random.seed(42) 
datos_experimento = [random.randint(1, 100) for _ in range(50)]

heap_resultado, heap_comparaciones, heap_intercambios, heap_tiempo = ejecutar_heapsort_minimos(datos_experimento)

print("Resultados Heapsort (Min-Heap):")
print("  • Lista ordenada:", heap_resultado)
print("  • Comparaciones:", heap_comparaciones)
print("  • Intercambios:", heap_intercambios)
print("  • Tiempo (segundos):", heap_tiempo)

# --- 2. Prueba Bucket Sort (5 vs 50 cubetas) ---
bucket5_resultado, bucket5_comparaciones, bucket5_intercambios, bucket5_tiempo = ejecutar_bucket_sort(datos_experimento, cantidad_cubetas=5)
bucket50_resultado, bucket50_comparaciones, bucket50_intercambios, bucket50_tiempo = ejecutar_bucket_sort(datos_experimento, cantidad_cubetas=50)

print("\nResultados Bucket Sort (5 cubetas):")
print("  • Comparaciones totales:", bucket5_comparaciones)
print("  • Tiempo (segundos):", bucket5_tiempo)

print("\nResultados Bucket Sort (50 cubetas):")
print("  • Comparaciones totales:", bucket50_comparaciones)
print("  • Tiempo (segundos):", bucket50_tiempo)