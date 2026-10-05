class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class PilaEnlazada:
    def __init__(self):
        self.cima = None
        self.tamaño = 0

    def apilar(self, valor):
        nuevo_nodo = NodoPila(valor)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        self.tamaño += 1

    def desapilar(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        valor = self.cima.dato
        self.cima = self.cima.siguiente
        self.tamaño -= 1
        return valor

    def consultar_cima(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        return self.cima.dato

    def esta_vacia(self):
        return self.cima is None

    def obtener_tamaño(self):
        return self.tamaño

class Recurso:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.estado = "Disponible"

    def __repr__(self):
        return f"Recurso({self.nombre}, Estado: {self.estado})"

class Prestamo:
    def __init__(self, id_prestamo, recurso):
        self.id_prestamo = id_prestamo
        self.recurso = recurso

class SistemaPrestamos:
    def __init__(self):
        self.hitorial_deshacer = PilaEnlazada()

    def registrar_prestamo(self, id_prestamo, recurso):
        if recurso.estado != "Disponible":
            print(f"El recurso {recurso.nombre} no está disponible para préstamo.")
            return

        recurso.estado = "Prestado"
        prestamo = Prestamo(id_prestamo, recurso)
        self.hitorial_deshacer.apilar(prestamo)

    def deshacer_ultimo_prestamo(self):
        if self.hitorial_deshacer.esta_vacia():
            print("No hay préstamos para deshacer.")
            return

        ultimo_prestamo = self.hitorial_deshacer.desapilar()
        ultimo_prestamo.recurso.estado = "Disponible"
        print(f"Se ha deshecho el préstamo del recurso {ultimo_prestamo.recurso.nombre}.")

if __name__ == "__main__":
    sistema = SistemaPrestamos()

    Libro1 = Recurso(1, "Libro de Matemáticas")
    Libro2 = Recurso(2, "Libro de Física")

    print("Estado inicial de los recursos:")
    print(Libro1)
    print(Libro2)


    print("\nRegistrando préstamos:")
    sistema.registrar_prestamo(101, Libro1)
    sistema.registrar_prestamo(102, Libro2)
    print(Libro1)
    print(Libro2)

    print("\nDeshaciendo el último préstamo:")
    sistema.deshacer_ultimo_prestamo()
    print(Libro1)
    print(Libro2)