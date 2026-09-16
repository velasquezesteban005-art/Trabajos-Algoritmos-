class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None


def imprimir_inverso(n):
    """Primero baja hasta el final, imprime al REGRESAR."""
    if n is None:                    # caso base: lista vacía
        return
    imprimir_inverso(n.sig)          # 1) resuelve la cola
    print(n.dato, end=" ")           # 2) luego imprime la cabeza


def imprimir_directo(n):
    """Mismo código con las dos líneas intercambiadas."""
    if n is None:
        return
    print(n.dato, end=" ")
    imprimir_directo(n.sig)


if __name__ == "__main__":
    cabeza = Nodo(1)
    cabeza.sig = Nodo(2)
    cabeza.sig.sig = Nodo(3)
    cabeza.sig.sig.sig = Nodo(4)

    print("Directo:", end=" "); imprimir_directo(cabeza); print()
    print("Inverso:", end=" "); imprimir_inverso(cabeza); print()