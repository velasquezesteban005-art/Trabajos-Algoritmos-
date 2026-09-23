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

def ordenar_registros_proyecto(registros):
    n = len(registros)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - i - 1):
            if registros[j]["veces_prestado"] > registros[j + 1]["veces_prestado"]:
                registros[j], registros[j + 1] = registros[j + 1], registros[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return registros

datos = [1, 2, 3, 4, 5, 6, 7, 8]
for nombre, funcion in [("Bubble Sort Optimizado", bubble_sort_optimizado)]:
    lista_ordenada, comparaciones, intercambios = funcion(datos.copy())
    print(f"{nombre}:")
    print(f"Lista ordenada: {lista_ordenada}")
    print(f"Comparaciones: {comparaciones}")
    print(f"Intercambios: {intercambios}\n")

mis_registros = [
    {"id": 101, "titulo": "Estructuras de Datos", "veces_prestado": 15},
    {"id": 102, "titulo": "Algoritmos en Python", "veces_prestado": 2},
    {"id": 103, "titulo": "Base de Datos", "veces_prestado": 27},
    {"id": 104, "titulo": "Redes de Computadoras", "veces_prestado": 8}
]

registros_ordenados = ordenar_registros_proyecto(mis_registros)

print("\n Registros ordenados por 'veces_prestado':")
for reg in registros_ordenados:
    print(f"  • ID: {reg['id']} | Titulo: {reg['titulo']} | Veces prestado: {reg['veces_prestado']}")