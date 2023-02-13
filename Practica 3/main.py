from ejercicios.ejercicio2 import *
from ejercicios.ejercicio3 import *
from ejercicios.ejercicio4 import *
from ejercicios.ejercicio6 import *
from ejercicios.ejercicio7 import *
#ejercicios8 incluye el import de os y ejercicio5
from ejercicios.ejercicio8 import *

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

    ejercicio2(sentece)
    ejercicio3(num1, num2)
    # ****Ejercicio 4**** #
    print("\n**** Se está ejecutando el ejercicio 4 ****")
    ejercicio4(Catalogo, producto1)
    ejercicio4(Catalogo, producto2)
    print("**** Se finaliza la ejecución del ejercicio 4 ****\n")

    ejercicio6()
    # ******* Ejercicio 7 ******* #
    print("\n******* Se está ejecutando el ejercicio 7 *******")
    # "producto1" es el nombre del producto, "PERU-0001-2023" es el código del producto
    ejercicio7("Producto 1", "PERU-0001-2023")
    ejercicio7("Producto 2", "PERU-0005-2024")
    print("******* Se está ejecutando el ejercicio 7 *******\n")

    ejercicio8(num1,num2)
    os.system("pause")  