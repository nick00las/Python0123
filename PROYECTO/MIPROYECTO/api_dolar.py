import requests
import csv

contador=0

for i in range (2019,2023):
    for j in range(1,13):
        year=i    
        if(j<10):
            month='0'+str(j)
        else:
            month=j

        url = f'https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={year}-{month}-20'
        response = requests.get(url)
        data = response.json()

        print(data)

        fecha=data["fecha"]
        dolar_compra = data["compra"]
        dolar_venta = data["venta"]

        if contador==0:
            with open('dolar_price.csv', 'w', newline='') as csvfile:
                
                writer = csv.writer(csvfile)
                writer.writerow(["Fecha", "Precio del Dolar (compra)","Precio del Dolar (venta)"])
                writer.writerow([fecha, dolar_compra, dolar_venta])
        else:
            with open('dolar_price.csv', 'a', newline='') as csvfile:         
                writer = csv.writer(csvfile)
                writer.writerow([fecha, dolar_compra, dolar_venta])
        contador+=1
    