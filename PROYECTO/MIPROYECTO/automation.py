import pandas as pd
import requests
import sqlite3
import matplotlib.pyplot as plt

def insertDataManual(valor):
    conn=sqlite3.connect('tienda.db')
    insert=f"INSERT INTO DOLAR(DOLAR_SOLES) VALUES('{valor}')"
    conn.execute(insert)
    conn.commit()

def insertDataAuto():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    response = requests.get(url)
    data = response.json()

    dolar_compra = data["compra"]
    
    conn=sqlite3.connect('tienda.db')
    insert=f"INSERT INTO DOLAR(DOLAR_SOLES) VALUES('{dolar_compra}')"
    conn.execute(insert)
    conn.commit()
    
    """#obtiene la ruta absoluta
     #print(os.getcwd())
    path_=os.getcwd()+'\dataTienda.csv'
    '''#conection a bd
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()'''
    print(path_)
    df = pd. read_csv (path_, sep = ";") 
    ### logica para insertar 
    for i,fila in df.iterrows():
        print(fila['ORDER_ID'])"""

def updateDolar(valor_dolar,valor_id):
    conn=sqlite3.connect('tienda.db')
    update=f"UPDATE DOLAR SET DOLAR_SOLES={valor_dolar} WHERE IDKEY={valor_id}"
    conn.execute(update)
    conn.commit()

'''
message="""
    1)Insertar data:
    2)Actualizar data del dolar
"""
'''
def graf_historico():
    conn=sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    cursor.execute("SELECT FECHA,DOLAR_SOLES FROM DOLAR")
    datos = cursor.fetchall()
    fecha = [fila[0] for fila in datos]
    dolar_soles = [fila[1] for fila in datos]
    # Crear el gráfico de barras
    plt.bar(fecha, dolar_soles)

    # Personalizar el gráfico si es necesario
    plt.title("Evolución Historica del precio del dolar")
    plt.xlabel("Etiqueta del eje X")
    plt.ylabel("Dolar en soles")

    # Mostrar el gráfico
    plt.show()

    # Cerrar la conexión con la base de datos
    conn.close()
    pass

while True:
    message="""
        1. Insertar Data Manualmente
        2. Insertar Data Automaticamente
        3. Actualizar Data por ID
        4. Crear gráfica de evolución del precio del dolar
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

    

