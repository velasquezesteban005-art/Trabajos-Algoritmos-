class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ColaEnlazada:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamaño += 1

    def desencolar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        valor = self.frente.dato
        self.frente = self.frente.siguiente
        self.tamaño -= 1
        if self.frente is None:
            self.final = None
        return valor

    def consultar_frente(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.frente.dato

    def esta_vacia(self):
        return self.frente is None

    def obtener_tamaño(self):
        return self.tamaño

if __name__ == "__main__":
    cola = ColaEnlazada()
    cola.encolar(10)
    cola.encolar(20)
    cola.encolar(30)

    print("Frente de la cola:", cola.consultar_frente()) 
    print("Tamaño de la cola:", cola.obtener_tamaño())    

    valor_desencolado = cola.desencolar()
    print("Valor desencolado:", valor_desencolado)       
    print("Nuevo frente de la cola:", cola.consultar_frente()) 
    print("Nuevo tamaño de la cola:", cola.obtener_tamaño())     

    print("Desencolando todos los elementos:")
    while not cola.esta_vacia():
        print(cola.desencolar())

    print("La cola está vacía:", cola.esta_vacia()) 
    print("Tamaño de la cola después de vaciarla:", cola.obtener_tamaño())

    print("Volviendo a encolar elementos:")
    cola.encolar(40)
    cola.encolar(50)
    print("Nuevo frente de la cola:", cola.consultar_frente())
    print("Nuevo tamaño de la cola:", cola.obtener_tamaño())

