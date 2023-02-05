import os


# Clase Catalogo y producto son el ejercicio 4
class producto:
    def __init__(self, name):
        self.name = name


class Catalogo:
    def __init__(self):
        self.Catalogo_producto = []

    def agregar_producto(self, product):
        self.Catalogo_producto.append(product)

    def mostrar_productos(self):
        for product in self.Catalogo_producto:
            print(" ", product.name, end=" ")


# Clase Producto del ejercicio 7
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


# Funcion1 de la pregunta 3
def multiply_2(number):
    return number * 2


# Funcion2 de la pregunta 3
def sum(num1, num2):
    return num1 + num2


def ejercicio2(sentece):
    print("\n** Se está inicializando el ejercicio 2 **")

    # split
    words = sentece.split()
    print("  Se está separando el sentece: ", words, "\n")

    # join
    joined_text = " ".join(words)
    print("  Se está uniendo el sentece: ", joined_text, "\n")

    # count
    occurrence_object = "sentece"
    ocurrence = sentece.count(occurrence_object)
    print(f"  las veces que '{occurrence_object}' aparece: ", ocurrence, "\n")

    # find
    find_object = "imprentas"
    index = sentece.find(find_object)
    print(f"  '{find_object}' fue encontrado en: ", index, "\n")

    # uppercase
    c_letter = sentece.upper()
    print("  el sentece en MAYUSCULAS: ", c_letter, "\n")

    # lowercase
    l_case = sentece.lower()
    print("  el sentece en minusculas: ", l_case, end=" ")

    print("** Acabando el ejercicio 2 **\n")


def ejercicio3(num1, num2):
    print("\n*** Se está ejecutando el ejercicio 3 ***")
    print(f" la multiplicacion de {num1} por 2 es :", multiply_2(num1))
    print(f" la suma {num1} y {num2} es :", sum(num1, num2))
    print("*** Se finaliza la ejecución del ejercicio 3 ***\n")


def ejercicio4(cat, producto):
    cat.agregar_producto(producto)
    cat.mostrar_productos()
    print("")


def ejercicio5(num1, num2):
    ''''#
    importando paquetes - ejercicio 5
    funciones division, suma_recursiva se encuentran en la carpeta paquetitos/operaciones
    #'''
    print("\n***** Se está ejecutando el ejercicio 5 *****")
    from paquetitos.operaciones import division, suma_recursiva

    sum_result = suma_recursiva(num2)
    divide_result = division(num1, num2)

    print("  La suma de los 5 primeros numeros es: ", sum_result)
    print(f"  la división de {num1} entre {num2} es: ", divide_result)
    print("***** Se finaliza la ejecución del ejercicio 5 *****")


def ejercicio6():
    print("\n****** Se está ejecutando el ejercicio 6 ******")
    # imprimiendo ubicación del archivo
    print(" ", __file__)
    print("****** Se está ejecutando el ejercicio 6 ******\n")


def pr_ejercicio7(p1):
    print("  País de origen:", p1.origin_country())
    print("  Número de lote:", p1.batch_number())


def gen_object_ejercicio7(name, code):
    return Producto(name, code)


def ejercicio7(name, code):
    p1 = gen_object_ejercicio7(name, code)
    print(" ", p1)
    pr_ejercicio7(p1)


def ejercicio8():
    try:
        print("// Estamos dentro del try de la pregunta 8 //", end="")
        ejercicio5(num1, num2)
    except ImportError:
        print("Error al importar las funciones")
    else:
        print("  Ruta del directorio de trabajo:", os.getcwd())
    finally:
        print("// Proceso terminado - ejercicio 8 finalizado //")


'''#////////////////////////////////////////////////////// #'''


# Ejercicio 1: crear la condición __name__==’__main__’ verifica que el script sea el principal y no uno importado
if __name__ == '__main__':
    sentece = '''
        Lorem Ipsum es simplemente el sentece de relleno de las imprentas y archivos de sentece. 
        Lorem Ipsum ha sido el sentece de relleno estándar de las industrias desde el año 1500, 
        cuando un impresor (N. del T. persona que se dedica num1 la imprenta) desconocido usó una 
        galería de senteces y los mezcló de tal manera que logró hacer un libro de senteces especimen
    '''

    num1 = 10
    num2 = 5

    # Crear un objeto dentro de un catálogo C_producto -pregunta 4
    Catalogo = Catalogo()
    # siendo "Arroz" el nombre de un producto
    producto1 = producto("Arroz")
    producto2 = producto("leche")

    # **Ejercicio 2** #
    ejercicio2(sentece)

    # ***Ejercicio 3*** #
    ejercicio3(num1, num2)

    # ****Ejercicio 4**** #
    print("\n**** Se está ejecutando el ejercicio 4 ****")
    ejercicio4(Catalogo, producto1)
    ejercicio4(Catalogo, producto2)
    print("**** Se finaliza la ejecución del ejercicio 4 ****\n")

    # ****** Ejercicio 6 ****** #
    ejercicio6()

    # ******* Ejercicio 7 ******* #
    print("\n******* Se está ejecutando el ejercicio 7 *******")
    # "producto1" es el nombre del producto, "PERU-0001-2023" es el código del producto
    ejercicio7("Producto 1", "PERU-0001-2023")
    ejercicio7("Producto 2", "PERU-0005-2024")
    print("******* Se está ejecutando el ejercicio 7 *******\n")

    # ******** Ejercicio 8 ******** #
    ejercicio8()

    os.system("pause")