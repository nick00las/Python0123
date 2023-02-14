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

def updateDolar(valor_dolar,valor_id):
    conn=sqlite3.connect('tienda.db')
    update=f"UPDATE DOLAR SET DOLAR_SOLES={valor_dolar} WHERE IDKEY={valor_id}"
    conn.execute(update)
    conn.commit()

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

