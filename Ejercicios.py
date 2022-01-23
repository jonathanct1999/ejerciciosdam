# Ejercicio 1

from ast import Import
from posixpath import split
from pydoc import stripid
import re


Nombre = "Juan"
Apellido = "Perez"
Balances = 53.44

print (("Hola %s %s . Tu balance es %.2f $") % (Nombre, Apellido, Balances))

# Ejercicio 2

fl = float("3.14")

print (type(fl))

st = str(fl)

print (type(st))

tf = float(1)

print (type(tf))

it = int(tf)

print (type(it))

bl =bool("hola")

print (type(bl))

ss = str(bl)

print (type(ss))

# Ejercicio 3

i = 10

s = "Hola"

f = 2.3

print (len(str(i)))

print (len(s))

print (len(str(f)))

# Ejercicio 4

prueba = "Hola Mundo"



print (prueba.strip()) 

print (split(prueba))

print (prueba.lower())

print (prueba.upper())

print (prueba.find("h"))

print (prueba.index("Hola"))

print (prueba.startswith("Hola"))

# Ejercicio 5

import re

qj = "En un lugar de la mancha, cuyo nombre no quier acordarme"

it = re.findall("a",qj)

print (len(it))

