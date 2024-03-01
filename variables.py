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

# Assegnare valori a più variabili mettendoli su una sola linea

x, y, z = 'Orange', 'Banana', 'Cherry'

print(x, y, z) # Orange Banana Cherry

# o dare il medesimo valore a più variabili

x = y = z = 'Apple'

print(x, y, z) # Apple Apple Apple

# UNPACKING: serve per estrarre i valori da una variabile.

fruits = ['apple', 'strawberry', 'pineapple']
x, y, z = fruits

print(x, y, z) # apple strawberry pineapple

""" PRINT() -> viene utilizzata per generare delle variabili stampate in console. 
               Queste possono essere restituite più di una alla volta mettendo una ',' per separarle. 
               Oppure si può utilizzare l'operatore '+' per generare più variabili.
"""
x = 'Python is awesome!'

print(x) # Python is awesome!

x = 'Python'
y = 'is'
z = 'awesome!'

print(x, y, z) # Python is awesome!

x = 'Python '
y = 'is '
z = 'awesome!'

print(x + y + z) # Python is awesome! -> se non presenti degli spazi dopo 'Python' e 'is', la scritta verrebbe: 'Pythonisawesome!'

# se si utilizzano i numeri nelle variabili, '+' verrà letto come operatore matematico.

x = 5
y = 10

print(x + y) # 15

# se si uniscono variabili 'int' e 'str', nella funzione print() bisognerà dividerle con una ',', perché se si utilizzerà l'operatore matematico '+' darà errore.

"""
x = 5
y = 'Sam'

print(x + y) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

x = 5
y = 'Sam'

print(x, y) # 5 Sam

# VARIBILI GLOBALI: possono essere sempre usate sia all'interno di funzioni che fuori.

x = 'SpAcE!'

def myfunc():
    print('The cat is in the... ' + x) # The cat is in the... SpAcE!

myfunc()