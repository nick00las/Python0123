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