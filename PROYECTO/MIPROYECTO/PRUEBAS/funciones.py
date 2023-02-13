'''import csv

def read_csv(file_name):
    data = []
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def print_data(data):
    print("\n".join("\t".join(row[col] for col in row) for row in data))

def add_data(file_name, data):
    fields = data[0].keys()
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writerow(data)'''

import pandas as pd

def menu():
    print("Menú de opciones")
    print("1. Ver la data")
    print("2. Buscar datos por fecha")
    print("3. Modificar un registro por fecha")
    print("4. Salir")
    
def ver_data(df):
    print(df)
    
def buscar_fecha(df):
    fecha = input("Ingrese la fecha que desea buscar (yyyy-mm-dd): ")
    result = df[df["Fecha"] == fecha]
    print(result)

def modificar_registro(df):
    fecha = input("Ingrese la fecha del registro que desea modificar (yyyy-mm-dd): ")
    result = df[df["Fecha"] == fecha]
    if result.empty:
        print("No se encontró ningún registro con la fecha especificada")
    else:
        dolar_compra = input("Ingrese el nuevo precio de compra: ")
        dolar_venta = input("Ingrese el nuevo precio de venta: ")
        result["Precio del Dolar (compra)"] = dolar_compra
        result["Precio del Dolar (venta)"] = dolar_venta
        df.update(result)
        print("Registro actualizado")

