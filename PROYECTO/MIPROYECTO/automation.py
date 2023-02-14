import pandas as pd
import os
import db
import requests
import sqlite3

def insertData():
    #obtiene la ruta absoluta
     #print(os.getcwd())
    path_=os.getcwd()+'\dataTienda.csv'
    '''#conection a bd
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()'''
    print(path_)
    df = pd. read_csv (path_, sep = ";") 
    ### logica para insertar 
    for i,fila in df.iterrows():
        print(fila['ORDER_ID'])

def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    response = requests.get(url)
    data = response.json()

    dolar_compra = data["compra"]
    
    conn=sqlite3.connect('tienda.db')
    insert=f"INSERT INTO DOLAR(DOLAR_SOLES) VALUES('{dolar_compra}')"
    conn.execute(insert)

'''
message="""
    1)Insertar data:
    2)Actualizar data del dolar
"""
'''

while True:
    message="""
        1. Opción 1
        2. Opción 2
    """
    print(message)
    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == "1":
        insertData()
    elif opcion == "2":
        updateDolar()
    else:
        print("Opción no válida. Selecciona de nuevo.")

    



