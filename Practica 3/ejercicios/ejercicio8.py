from ejercicios.ejercicio5 import *
import os

def ejercicio8(num1,num2):
    
    try:
        print("// Estamos dentro del try de la pregunta 8 //", end="")
        ejercicio5(num1, num2)
    except ImportError:
        print("Error al importar las funciones")
    else:
        print("  Ruta del directorio de trabajo:", os.getcwd())
    finally:
        print("// Proceso terminado - ejercicio 8 finalizado //")