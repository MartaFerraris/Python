# DATA TYPES:

"""
BUILT-IN TYPES:
    Text: 'str'
    Numeric: 'int', 'float', 'complex'
    Sequence: 'list', 'tulpe', 'range'
    Mapping: 'dict'
    Set: 'set', 'frozenset'
    Boolean: 'bool'
    Binary: 'bytes', 'bytearray', 'memoryview'
    None: 'NoneType'
"""

# capire il tipo del dato

x = 5

print(type(x)) # <class 'int'>

# Setting data type:

x = 'Hello World!'                          # -> <class 'str'>
x = 20                                      # -> <class 'int'>
x = 20.5                                    # -> <class 'float'>
x = 1j                                      # -> <class 'complex'>
x = ['red', 'blue', 'green']                # -> <class 'list'>
x = ('red', 'blue', 'green')                # -> <class 'tuple'>
x = range(4)                                # -> <class 'range'>
x = {'name': 'Jerry', 'animal': 'mouse'}    # -> <class 'dict'>
x = {'red', 'blue', 'green'}                # -> <class 'set'>
x = frozenset({'red', 'blue', 'green'})     # -> <class 'frozenset'>
x = True                                    # -> <class 'bool'>
x = b'Hello'                                # -> <class 'bytes'>
x = bytearray(4)                            # -> <class 'bytearray'>
x = memoryview(bytes(3))                    # -> <class 'memoryview'>
x = None                                    # -> <class 'NoneType'>

print(type(x))

# Setting specific data type:

y = str('Hello World!')                     # -> <class 'str'>
y = int(20)                                 # -> <class 'int'>
y = float(20.5)                             # -> <class 'float'>
y = complex(1j)                             # -> <class 'complex'>
y = list(('red', 'blue', 'green'))          # -> <class 'list'>
y = tuple(('red', 'blue', 'green'))         # -> <class 'tuple'>
y = range(4)                                # -> <class 'range'>
y = dict(name='Jerry', animal='mouse')      # -> <class 'dict'>
y = set(('red', 'blue', 'green'))           # -> <class 'set'>
y = frozenset(('red', 'blue', 'green'))     # -> <class 'frozenset'>
y = bool(4)                                 # -> <class 'bool'>
y = bytes(4)                                # -> <class 'bytes'>
y = bytearray(4)                            # -> <class 'bytearray'>
y = memoryview(bytes(4))                    # -> <class 'memoryview'>

print(type(y))