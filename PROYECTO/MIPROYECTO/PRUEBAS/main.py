from funciones import *
'''

    file_name = 'dolar_price.csv'
    data = read_csv(file_name)
    while True:
        print("1. Ver data")
        print("2. Actualizar data")
        print("3. Salir")
        choice = input("Elija una opción: ")
        if choice == '1':
            print_data(data)
        elif choice == '2':
            new_data = input("Ingrese la nueva data en formato 'col1,col2,col3': ")
            new_data = new_data.split(',')
            add_data('dolar_price.csv', new_data)
            data = read_csv('dolar_price.csv')
        elif choice == '3':
            break
        else:
            print("Opción inválida.")
'''
if __name__ == '__main__':
    df = pd.read_csv("dolar_price.csv")

    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            ver_data(df)
        elif opcion == 2:
            buscar_fecha(df)
        elif opcion == 3:
            modificar_registro(df)
        elif opcion == 4:
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            
    df.to_csv("dolar_price.csv", index=False)