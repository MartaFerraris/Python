# STRING:

print("Hello")
print('World')

# Assegnare una stringa a una variabile

a = 'Cat'
print(a)

# Stringhe multiple

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)

# Array di stringhe
# Le parentesi quadre possono essere 
# utilizzate per accedere agli elementi della stringa.

d = 'Hello, mountains!'
print(d[1], d[10])  # e n

# Ciclo attraverso una stringa
# Poiché le stringhe sono array, possiamo scorrere i caratteri in una stringa, con un ciclo for.

for x in 'banana':
    print(x)

'''
terminale:
b
a
n
a
n
a
'''

# Lunghezza della stringa
# Per ottenere la lunghezza di una stringa si utilizza la funzione len().
    
print(len(b))   # 123

# Controllo sulla stringa
# Per verificare se una determinata frase o carattere è presente in una stringa possiamo utilizzare la parola chiave 'in'.

txt = 'The best things in life are free!'
print('free' in txt)    # True

# Uso in un'istruzione 'if':

txt = 'The best things in life are free!'
if 'free' in txt:
    print('Yes is present.')    # Yes is present.

# Controllo con 'not in'
# Per verificare se una determinata frase o carattere 
# NON è presente in una stringa possiamo utilizzare la parola chiave not in.
    
txt = 'The best things in life are free!'
print('expensive' not in txt)   # True

# Usando if:

txt = 'The best things in life are free!' 
if 'expensive' not in txt:
    print('No, is not present.') # No, is not present.

#-------------------------------------------------------------------------------------------------------------------

# DIVISIONE DELLA STRINGA
# È possibile restituire un intervallo di caratteri utilizzando la sintassi della sezione.
# Specificare l'indice iniziale e l'indice finale, separati da due punti, per restituire una parte della stringa.

e = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit'''
print(e[2:5])   # rem

# Divisione dall'inizio
# Tralasciando l'indice iniziale, l'intervallo inizierà dal primo carattere:

print(e[:5])    # Lorem

# Divisione dalla fine
# Tralasciando l'indice finale, l'intervallo arriverà alla fine:

print(e[2:])    # rem ipsum dolor sit amet, consectetur adipiscing elit

# Indice negativo
# Utilizzando gli indici negativi per iniziare la sezione dalla fine della stringa:

print(e[-5:-2]) # ' el'

#-------------------------------------------------------------------------------------------------------------------

# MODIFICA DELLE STRINGHE

# UPPER-CASE

a = 'Hello, World!'
print(a.upper())    # HELLO, WORLD!

# LOWER-CASE

a = 'Hello, World!'
print(a.lower())    # hello, world!

# RIMOZIONE DELLO SPAZIO

a = ' Hello, World! '
print(a.strip())    # 'Hello, World!'

# RIMPIAZZO DELLA STRINGA

a = 'Hello, World!'
print(a.replace('H', 'J'))    # 'Jello, World!'

# DIVISIONE DELLE STRINGHE

a = 'Hello, World!'
print(a.split(','))    # ['Hello', ' World!']

#-------------------------------------------------------------------------------------------------------------------

# STRINGHE CONCATENATE
# Per concatenare, o combinare, due stringhe è possibile utilizzare l'operatore +.
# Unire la variabile 'a' con la variabile 'b' nella variabile 'c':

a = "Hello"
b = "World"
c = a + b
print(c)    # HelloWorld

# Per aggiungere uno spazio tra di loro, si aggiunge un " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)    # Hello World

#-------------------------------------------------------------------------------------------------------------------

# FORMATO STRINGHE

'''
Per combinare stringhe, numeri e booleani di utilizza il metodo format().
Al metodo format() si passano gli argomenti attraverso il placeholder {}. 
'''

age = 36
txt = 'My name is Pino, and I am {}'
print(txt.format(age))

boolean = True
txt1 = 'This boolean is: {}'
print(txt1.format(boolean))

'''
Il metodo format() può tenere un numero illemitato di argomenti, collocandoli nei loro rispettivi placeholders.
'''

qnty = 3
itemno = 567
price = 49.95
myorder = 'I want {} pieces of item {} for {} dollars.'
print(myorder.format(qnty, itemno, price))

'''
Si possono usare gli indici {0} per essere sicuri che gli argomenti siano nel posto corretto.
'''

qnty = 3
itemno = 567
price = 49.95
myorder = 'I want to pay {2} dollar for {0} pieces of item {1}.'
print(myorder.format(qnty, itemno, price))

#-------------------------------------------------------------------------------------------------------------------

# ESCAPE CHARACTERS

'''
Per inserire caratteri non validi in una stringa, si utilizza un carattere di escape [\] seguito poi dal carattere che si desidera inserire.
Esempio di carattere non valido è una virgoletta doppia [" "] all'interno di una stringa racchiusa tra due virgolette doppie.

Es di errore:
txt = "We are the so-called "Vikings" from the north."
'''

txt2 = "We are the so-called \"Vikings\" from the north."
