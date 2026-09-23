def bubble_sort_optimizado(lista):
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    
    for i in range(n):
        hubo_intercambio = False  
        
        for j in range(0, n - i - 1):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                # Intercambio en Python
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
                hubo_intercambio = True
        
        if not hubo_intercambio:
            break
            
    return lista, comparaciones, intercambios

datos = [1, 2, 3, 4, 5, 6, 7, 8]
for nombre, funcion in [("Bubble Sort Optimizado", bubble_sort_optimizado)]:
    lista_ordenada, comparaciones, intercambios = funcion(datos.copy())
    print(f"{nombre}:")
    print(f"Lista ordenada: {lista_ordenada}")
    print(f"Comparaciones: {comparaciones}")
    print(f"Intercambios: {intercambios}\n")