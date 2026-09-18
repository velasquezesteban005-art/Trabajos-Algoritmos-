# comparo dos vecinos si estan al reves los intercambio y repito el proceso 
# hast que nadie mas se mueva bubble sort

def bubble_sort(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
                swapped = True
        if not swapped:
            break
    return arr, comparaciones, intercambios
#buscar el más pequeño y ponerlo al 
# principio selection sort

def selection_sort(arr):
    n = len(arr)
    comparaciones= 0
    intercambios = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        intercambios += 1
    return arr, comparaciones, intercambios
# tomo el segubndo y lo inserto donde va 
# respecto al primero insertion sort

def insertion_sort(arr):
    comparaciones = 0
    intercambios = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparaciones += 1
            arr[j + 1] = arr[j]
            intercambios += 1
            j -= 1
        arr[j + 1] = key
    return arr, comparaciones, intercambios

# datos: [64, 25, 12, 22, 11, 90, 45, 33]
datos = [64, 25, 12, 22, 11, 90, 45, 33]
for nombre, funcion in [("Bubble", bubble_sort), ("Selection", selection_sort), ("Insertion", insertion_sort)]:
    resultado, comp, interc = funcion(datos.copy())
    print(f"{nombre} sort > {resultado}")
    print(f" Comparaciones: {comp},  Intercambios: {interc}")