import pandas as pd
from f_usuario import * 
from f_dolar import * 


while True:
    message="""
        1. Insertar Data Manualmente
        2. Insertar Data Automaticamente
        3. Actualizar Data por ID
        4. Crear gráfica de evolución del precio del dolar
        5. Trabajar la data de los usuarios
    """
    print(message)
    opcion = input("Selecciona una opción (1,2,3 o 4): ")

    if opcion == "1":
        try:
            valor_dolar=input("Ingrese el valor del dolar en soles: ")
            insertDataManual(valor_dolar)
        except: 
            print("Error")
        else:
            print("se inserto correctamente")
    elif opcion == "2":
        try:
            insertDataAuto()
        except: 
            print("Error")
        else:
            print("se inserto correctamente")

    elif opcion == "3":
        try:
            valor_dolar=input("Ingrese el valor del dolar en soles: ")
            valor_id=input("Ingrese la ID que quiere reemplazar: ")
            updateDolar(valor_dolar,valor_id)
        except: 
            print("Error")
        else:
            print("se actualizo correctamente")
    elif opcion == "4":
        graf_historico()
    else:
        exit()

    

