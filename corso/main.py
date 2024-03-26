#Semplice metodo per mandare a schermo qualcosa
"""
messaggio = input('Inserisci qualcosa: ')

print(messaggio)
"""

#--------------------------------------------------------------------------

""" 
if 1 < 5:
    print('messaggio') 
"""

#--------------------------------------------------------------------------

""" 
03 - Variabili
    - cos'è e come creare una variabile;
    - nomenclatura: regole o pratiche per determinare le variabili;
    - assegnare multipli valori;
    - utilizzare una variabile;
"""

""" 
TIPO DI VARIABILI:
GIUSTI:
    pesopersona
    peso_persona
    _peso_persona
    pesoPersona
    PESOPERSONA
    pesopersona2 

SBAGLIATI:
2pesopersona
peso-persona
peso persona
"""
città = ['Roma', 'Milano', 'Napoli']
x, y, z = 32, 100, 987
#print(x, y, z)

x1 = y1 = z1 = 23
#print(x1, y1, z1)

città = ['Roma', 'Milano', 'Napoli']
x2, y2, z2 = città
#print(x2, y2, z2)

x3 = 32
y3 = 8
z3 = x + y + x + x
#print(z3)

#--------------------------------------------------------------------------

""" 
04 - Tipi di dati
    - ottenere il tipo di dato;
    - come viene assegnato il tipo;
    - tipi di dato;
"""

x = 5
#print(type(x))

x = 'Ciao'
#print(type(x))

x = False
#print(type(x))

#--------------------------------------------------------------------------

""" 
05 - Casting
    - cosa vuol dire castare;
    - quando si fa;
    - come con int(), float(), str();
"""

x = 5
y = int('54645')
#print(x + y)

x = float(5)
#print(x)

#--------------------------------------------------------------------------

""" 
06 - Stringhe
    - crare una stringa, parlare di apici doppi singoli;
    - mandare a schermo stringa e variabili stringa;
    - stringhe multi riga;
    - trattare stringhe come array (prendere carattere, length, loop)

    - prendere parte di stringa str[:5], str[:2], str[-5:-2];
    - modificare stringa con upper(), lower(), strip(), split(), e replace();
    - concatenare stringhe;
    - usare format() per combinare stringhe e numeri;
    - escape dei caratteri;
"""

x = 'prova'
y = "ciao"
#print(x[0])

x = 'Ciao sono Pinco Pallino'
#print(len(x))

print(x[:3])
print(x[2:])
print(x[2:7])
print(x.upper())
print(x.lower())
print(x.strip())
print(x.replace('o', 'w'))