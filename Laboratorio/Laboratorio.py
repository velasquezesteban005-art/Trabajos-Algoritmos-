import time
mapa = [
    [0, 0, 2, 0, 0],
    [0, 1, 0, 0, 2],
    [0, 0, 0, 1, 0],
    [2, 0, 1, 0, 0],
    [0, 0, 1, 2, 0],
]

movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def imprimir_mapa(mapa, camino):
    camino_set = set(camino)
    for r, fila in enumerate(mapa):
        linea = ""
        for c, val in enumerate(fila):
            if (r, c) in camino_set:
                linea += " * "
            elif val == 1:
                linea += " # "
            elif val == 2:
                linea += " o "
            else:
                linea += " . "
        print(linea)
    print()


def buscar_camino(mapa, contar_todos=False):
    filas, cols = len(mapa), len(mapa[0])
    salida = (filas - 1, cols - 1)
    visitado = [[False] * cols for _ in range(filas)]
    camino = []
    primer_camino = []
    total = [0]

    def backtrack(r, c):
        if not (0 <= r < filas and 0 <= c < cols):
            return False
        if mapa[r][c] == 1 or visitado[r][c]:
            return False

        visitado[r][c] = True
        camino.append((r, c))

        encontrado = False
        if (r, c) == salida:
            total[0] += 1
            if not primer_camino:
                primer_camino.extend(camino)
            encontrado = True
        else:
            for dr, dc in movimientos:
                if backtrack(r + dr, c + dc):
                    encontrado = True
                    if not contar_todos:
                        break

        camino.pop()
        visitado[r][c] = False
        return encontrado

    backtrack(0, 0)
    return primer_camino, total[0]

def recoger_puntos(mapa, contar_todos=False):
    filas, cols = len(mapa), len(mapa[0])
    salida = (filas - 1, cols - 1)
    puntos = [(r, c) for r, fila in enumerate(mapa) for c, v in enumerate(fila) if v == 2]
    mascara_completa = (1 << len(puntos)) - 1
    indice = {pos: i for i, pos in enumerate(puntos)}

#
    visitados = set()
    camino = []
    primer_camino = []
    total = [0]

    def backtrack(r, c, mascara):
        if not (0 <= r < filas and 0 <= c < cols):
            return False
        if mapa[r][c] == 1:
            return False

        if (r, c) in indice:
            mascara |= (1 << indice[(r, c)])

        estado = (r, c, mascara)
        if estado in visitados:
            return False
        visitados.add(estado)
        camino.append((r, c))

        encontrado = False
        if (r, c) == salida and mascara == mascara_completa:
            total[0] += 1
            if not primer_camino:
                primer_camino.extend(camino)
            encontrado = True
        else:
            for dr, dc in movimientos:
                if backtrack(r + dr, c + dc, mascara):
                    encontrado = True
                    if not contar_todos:
                        break

        camino.pop()
        visitados.discard(estado)
        return encontrado

    backtrack(0, 0, 0)
    return primer_camino, total[0]


if __name__ == "__main__":
    puntos = [(r, c) for r, fila in enumerate(mapa) for c, v in enumerate(fila) if v == 2]

    print("Camino sin recoger puntos:")
    inicio = time.perf_counter()
    camino1, total1 = buscar_camino(mapa, contar_todos=True)
    fin = time.perf_counter()
    imprimir_mapa(mapa, camino1)
    recogidos1 = set(camino1) & set(puntos)
    print(f"Puntos recogidos: {len(recogidos1)} de {len(puntos)}")
    print(f"Caminos encontrados: {total1}")
    print(f"Tiempo: {fin - inicio:.6f} s\n")

    print("Camino recogiendo todos los puntos:")
    inicio = time.perf_counter()
    camino2, total2 = recoger_puntos(mapa, contar_todos=True)
    fin = time.perf_counter()
    if camino2:
        imprimir_mapa(mapa, camino2)
        recogidos2 = set(camino2) & set(puntos)
        print(f"Puntos recogidos: {len(recogidos2)} de {len(puntos)}")
    else:
        print("No hay camino que recoja todos los puntos.")
    print(f"Caminos encontrados: {total2}")
    print(f"Tiempo: {fin - inicio:.6f} s")