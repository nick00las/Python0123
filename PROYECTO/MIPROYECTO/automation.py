import pandas as pd
from f_usuario import * 
from f_dolar import * 
import os

while True:
    message="""
        1. Insertar Data Manualmente
        2. Insertar Data Automaticamente
        3. Actualizar Data por ID
        4. Crear gráfica de evolución del precio del dolar
        5. Crear usuario
        6. Eliminar usuario
        7. Actualizar usuario
        0. Salir
    """
    print(message)
    opcion = input("Selecciona una opción (0,1,2,3,4,5,6 o 7): ")

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
    elif opcion == "5":
        try:
            crear_usuario()
        except: 
            print("Error")
        else:
            print("se creo el usuario correctamente")
    elif opcion == "6":
        try:
            usuario=input("Ingrese el 'usuario' que desea eliminar: ")
            eliminar_usuario(usuario)
        except: 
            print("Error")
        else:
            print("se elimino el usuario correctamente")
    elif opcion == "7":
        try:
            usuario=input("Ingrese el 'usuario' que desea actualizar: ")
            email=input("Ingrese la nueva direccion de correo: ")
            update_usuario(usuario,email)
        except: 
            print("Error")
        else:
            print("se actualizó el usuario correctamente")
    elif opcion == "0":
        exit()
    else:
        print("Seleccionaste una opción inválida, intente de nuevo")

    

