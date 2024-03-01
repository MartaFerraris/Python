# VARIABILI DI PYTHON

# Creare una variabile
# Si crea una variabile nel momento in cui si assegna un valore ad essa.

x = 5
y = "John"

print(x)
print(y)

# le variabili non hanno un tipo e glielo si può cambiare risettandole

xx = 4          # xx è di tipo int 
xx = "Sally"    # xx adesso è di tipo str

print(xx)

# per specificare il tipo di variabile si vuole lo si può fare con il casting 

x = str(3)    # x sarà '3'
y = int(3)    # y sarà 3
z = float(3)  # z sarà 3.0

print(x, y, z)

# si può ottenere il tipo di variabile attraverso la funzione type()

x = 5       # class 'int'
y = "John"  # class 'str'

print(type(x), type(y))

# la dichiarazione di una stringa può avvenire o attraverso le singole virgolette ('') o con le doppie ("")

x = "John"
x = 'John'

# se le variabili vengono nominate con maiuscole non sovrascriveranno quelle con la minuscola

a = 4
A = 'Sally'

"""
REGOLE PER IL NOME DELLE VARIABILI:
    1- deve iniziare con una lettera o con un underscore;
    2- non deve iniziare con un numero;
    3- può contenere valori alfanumerici e underscore (A-z, 0-9 e _);
    4- CASE-SENSITIVE: sono distinti tra maiuscole e minuscole (età, Età  e ETÀ -> sono variabili diverse);
    5- il nome non può essere una delle Python keywords.

esempio:
"""

myvar = 'Hello!'
my_var = 'Hello!'
_my_var = 'Hello!'
myVar = 'Hello!'
MYVAR = 'Hello!'
myvar2 = 'Hello!'

"""
TECNICHE PER RENDERE PIU'LEGGIBILE IL CODICE:
    1- CAMEL-CASE;
    2- PASCAL-CASE;
    3- SNAKE-CASE;
"""

myVarName = 'John'
MyVarName = 'John'
my_var_name = 'John'