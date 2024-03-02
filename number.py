# NUMBERS

"""
Numbers type:
    - int
    - float
    - complex
"""

# INT: Int, o intero, è un numero intero, positivo o negativo, senza decimali, di lunghezza illimitata.

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# FLOAT: o "numero in virgola mobile" è un numero, positivo o negativo, contenente uno o più decimali.

x = 1.10
y = 1.0
z = -35.59
a = 35e3
b = 12E4
c = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))

# COMPLEX: i numeri complessi si scrivono con una "j" come parte immaginaria

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# CONVERSIONE DEL TIPO:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# conversione da int a float:
a = float(x)

# conversione da float a int:
b = int(y)

# conversione da int a complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Python non ha una random() funzione per creare numeri casuali, ma Python ha un modulo 
# integrato chiamato randomche può essere utilizzato per creare numeri casuali:

import random

print(random.randrange(1, 10))