from calendar import prmonth
import re

from sys import argv

script, user = argv

ss = str(user)

prmonth = '>'

print ("Escriba una frase")

fr = str(input(prmonth))

print ("Escriba letra a buscar")

lt = str(input(prmonth))

it = re.findall(lt,fr)

print ("Cual es tu edad")

ed = int(input(prmonth))

print ("Que hora es")

hr = int(input(prmonth))

print (" %s  su frase  %s  contiene %d  %s , tienes %d años y son las %d ") % (ss,fr,it,lt,ed,hr)


print (''' %s  su frase  %s  contiene %d  %s, tienes %d años y son las %d ''') % (ss,fr,it,lt,ed,hr)


