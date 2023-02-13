import sys

##ROJAS GALA NICOLAS ALONSO EJERCICIO 1 SEMANA 1 
print("pregunta 1 ")

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
DNI=input("Ingrese su DNI: ")

print("Hola ",nombre," ",apellido," con D.N.I ",DNI)

##ROJAS GALA NICOLAS ALONSO EJERCICIO 2 SEMANA 1 
import math

print("pregunta 2")
radio=int(input("Ingrese el radio: "))

print("area de circulo", radio*radio*math.pi)
print("area de cuadrado", radio*radio)
print("area del triangulo equilatero", radio*radio/4*math.sqrt(3))

##ROJAS GALA NICOLAS ALONSO EJERCICIO 3 SEMANA 1 
print("pregunta 3")
val1=float(input("Ingrese el valor 1: "))
val2=float(input("Ingrese el valor 2: "))
val3=float(input("Ingrese el valor 3: "))

print("la suma de los 3 valores es ", val1+val2+val3)
print("la resta de los 3 valores es ", val3-val2-val1)
print("la multiplicación de los 3 valores es ", val1*val2*val3)
print("la division de los valores es: ", val1/val2/val3)
print("la division entera de los valores es: ", val1//val2//val3)

print("pregunta 4")
dato=input("Ingrese un valor(sin importar tipo de dato): ")

if isinstance(dato, int):
    data_type = "<class 'int'>"
elif isinstance(dato, str):
    data_type = "<class 'str'>"
elif isinstance(dato, list):
    data_type = "<class 'list'>"
elif isinstance(dato, float):
    data_type = "<class 'float'>"
elif isinstance(dato, dict):
    data_type = "<class 'dict'>"
elif isinstance(dato, tuple):
    data_type = "<class 'tuple'>"
else:
    data_type = "Tipo de dato desconocido"

print(data_type)

##ROJAS GALA NICOLAS ALONSO EJERCICIO 5 SEMANA 1 
print("pregunta 5")
variable=sys.argv[0]
print(variable)

##ROJAS GALA NICOLAS ALONSO EJERCICIO 6 SEMANA 1 
print("pregunta 6")
rango=int(input("Ingrese un valor: "))
suma=0

for i in range(1,rango+1):
    suma=suma+i

print("la suma de los ", rango, " primeros numeros es: ",suma)

##ROJAS GALA NICOLAS ALONSO EJERCICIO 7 SEMANA 1 
print("pregunta 7")
num1=int(input("ingrese un numero 1: "))
num2=int(input("ingrese un numero 2: "))

if(num1==num2):
    print("los numeros son iguales")
else:
    print("los dos numeros son distintos")
    if(num1>num2):
        print("el numero 1 es mayor al numero 2")
    else:
        print("el numero 2 es mayor al numero 1")

##ROJAS GALA NICOLAS ALONSO EJERCICIO 8 SEMANA 1 
print("pregunta 8")

clave="contraseña"
clave_ingresada=input("ingrese la contraseña: ")

if(clave_ingresada.lower()==clave):
    print("las claves coinciden")
else:
    print("las claves NO coinciden")