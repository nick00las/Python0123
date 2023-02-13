# Clase Catalogo y producto son el ejercicio 4
class producto:
    def __init__(self, name):
        self.name = name

def ejercicio4(cat, producto):
    cat.agregar_producto(producto)
    cat.mostrar_productos()
    print("")