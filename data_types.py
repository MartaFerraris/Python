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
x = ('red', 'blue', 'green')                # -> <class 'tulpe'>
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