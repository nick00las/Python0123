# Clase Producto del ejercicio 7

#Clase Producto y Catalogo del ejercicio 7
class Producto:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"Producto: {self.name}, Código: {self.code}"

    def origin_country(self):
        # Buscamos el primer '-' para hacer un split
        return self.code.split("-")[0]

    def batch_number(self):
        # Buscamos el segundo '-' para hacer un split
        return self.code.split("-")[1]

class Catalogo:
    def __init__(self):
        self.Catalogo_producto = []

    def agregar_producto(self, product):
        self.Catalogo_producto.append(product)

    def mostrar_productos(self):
        for product in self.Catalogo_producto:
            print(" ", product.name, end=" ")
            
def pr_ejercicio7(p1):
    print("  País de origen:", p1.origin_country())
    print("  Número de lote:", p1.batch_number())


def ejercicio7(name, code):
    p1 = Producto(name, code)
    print(" ", p1)
    pr_ejercicio7(p1)