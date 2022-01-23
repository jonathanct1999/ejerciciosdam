#Ejercicio 2

from calendar import prmonth

prmonth = '>'

print ("Escriba un numero : ")

numero = int(input(prmonth))

nume = 1; 

while numero >= 0 :

    print (numero)
    numero = numero - nume

# Ejercicio 3

print ("Escriba un numero : ")

numero = int(input(prmonth))
 
num = 0

while num <= numero :

    if num % 2 == 0 :

         num = num + 1

    else :

        print (num)
        num = num + 1

# Ejercicio 4
    
nc = 1

while nc <= 10 :

    print ("Tabla del ", nc)

    dt = nc * 0

    print (dt)

    dt = nc * 1

    print (dt)

    dt = nc * 2

    print (dt)

    dt = nc * 3

    print (dt)

    dt = nc * 4

    print (dt)

    dt = nc * 5

    print (dt)

    dt = nc * 6

    print (dt)

    dt = nc * 7

    print (dt)

    dt = nc * 8

    print (dt)

    dt = nc * 9

    print (dt)

    dt = nc * 10

    print (dt)

    nc = nc + 1

# Ejercicio 5 


eco = ""


while eco != "Salir" :

    print ("Escriba una frase : ")
    eco = str(input(prmonth))
    print (eco)