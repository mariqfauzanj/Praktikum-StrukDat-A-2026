# datatypes.py / Python Data Types

# String
a = "Dibalik Awan!"
a = str("Dibalik Awan!")
print(type(a))  # output : <class 'str'>

# Integer
b = 2020
b = int(2020)
print(type(b))  # output : <class 'int'>

# Float
c = 20.5
c = float(20.5)
print(type(c))  # output : <class 'float'>

# Complex
d = 3j
d = complex(3j)
print(type(d))  # output : <class 'complex'>

# Other Data Types
e = ["batu", "gunting", "shotgun"]
e = list(["batu", "gunting", "shotgun"])
print(type(e))  # output : <class 'list'>

# Tuple
f = ("gandum", "susu", "gula", "telur")
f = tuple(("gandum", "susu", "gula", "telur"))
print(type(f))  # output : <class 'tuple'>

# Range
g = range(10)
print(type(g))  # output : <class 'range'>

# Dictionary
h = {"nama": "Ariq", "umur": 19}
h = dict(nama="Ariq", umur=19)
print(type(h))  # output : <class 'dict'>

# Set
i = {"T-34-85", "Tiger II", "M4A3 Sherman"}
i = set(("T-34-85", "Tiger II", "M4A3 Sherman"))
print(type(i))  # output : <class 'set'>

# Frozenset
j = frozenset({"Nikmati", "Saja", "Dulu"})
print(type(j))  # output : <class 'frozenset'>

# Boolean
k = True
k = bool(True)
print(type(k))  # output : <class 'bool'>

# Bytes
l = b"Hello!"
l = bytes(5)
print(type(l))  # output : <class 'bytes'>

# Bytearray
m = bytearray(15)
print(type(m))  # output : <class 'bytearray'>

# Memory View
n = memoryview(bytes(15))
print(type(n))  # output : <class 'memoryview'>

# None Type
o = None
print(type(o))  # output : <class 'NoneType'>