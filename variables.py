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

x = 5
y = "John"

print(type(x), type(y))