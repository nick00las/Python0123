## Pregunta 1


def menu1():
    n=5 ##N es la medida del lado del cuadrado
    print(" ")  
    for i in range(1,n+1):
        for j in range (1,n+1):
            print ("*",end="")
        print(" ")        
    print(" ")  

def menu2():
    numeros=[1,2,3,4,5,6,7,8,9,10]

    for numero in numeros:
        if numero%2==0:
            print(numero)
    
def menu3():
    personas =[("Nicolas",21),("Claudia",22),("Juan",17),("Rodrigo",23)]

    for persona in personas:
        nombre,edad=persona
        if edad>=18:
            print(f"{nombre} tiene {edad} años y por eso, es mayor de edad ")


while True:
    print("***Menu princiapal***")
    print("1. Dibujar cuadrado con *")
    print("2. Identifica si el numero es multiplo de 2")
    print("3. Iterar una lista de elementos. Imprimir mayores de edad")
    opc=input("Ingrese una opción: ")
    
    
    if opc=="1":
        menu1()
    elif opc=="2":
         menu2()
    elif opc=="3":
         menu3()