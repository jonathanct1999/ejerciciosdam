# Ejercicio 2

from calendar import prmonth
from distutils.log import error
import errno


prmonth = '>'

print ("Escriba su Edad : ")

edad = int(input(prmonth))

if edad > 18 :

    print ("Eres mayor de edad")

else :

    print ("Eres menor de edad")    


# Ejercicio 3

contraseña = "contrasena"

print ("Escriba la Contraseña : ")

con = str(input(prmonth))

if con.lower() == contraseña.lower() : 

    print ("Contraseña Correcta")

else :

    print ("Contraseña incorrecta")

# Ejercicio 4

print ("Escriba un numero Entero : ")

entero = int(input(prmonth))

if entero % 2 == 0 :

    print ("El  numero es par")

else :

    print ("El numero es impar")

# Ejercicio 5

print ("Escriba el dividendo  : ")

primero = int(input(prmonth))

print ("Escriba el divisor  : ")

segundo = int(input(prmonth))

if segundo == 0 :

   print (ZeroDivisionError)

else :


     resultado = primero / segundo

     print ("El resultado es ", resultado)