#Anotar una secuencia de paso de un algoritmo 
#1. Que es n en esa secuencia?
#2. Cuantas veces se ejecuta el proceso si se duplicna los datos?
#3. Dentro de esa secuencia se invoca otro proceso?
#4. Que tipo de estructura de datos se utiliza

#1. n es la cantidad de elementos en el arreglo arr que se va a ordenar.
#2. Buble sort es O^(n^2), por lo que si duplicamos los datos, el tiempo de ejecución se cuadruplica.
#3. Dentro de bubble_sort se invoca el proceso Len el cual tiene un nivel de complejidad O(1)
#4. Se utiliza una lista o arreglo, para poder acceder a cualquier elemento del arreglo y poder compararlos entre si.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
#En la funcion bubble_sort encontramos varios niveles de complejidad, el primero lo en contramos en la linea 14 que es n = len(arr). esta linea tiene un nivel de complejidad O(1)
#Luego en la linea 15 encontramos un fro con nivel de complejidad O(n) pero dentro de ese for encontramos otro for con nivel de complejidad O(n),
#esto hace que el for sea anidado y por lo tanto el nivel de complejidad de ese for es O(n^2)
#Luego encontramos un if con nivel de complejidad O(1) y dentro de ese if tenemos otro if con el mismo nivel de complejidad.
#Si multiplicamos los niveles de complejidad de cada linea, obtenemos que el nivel de complejidad de la funcion bubble_sort es O(n^2)