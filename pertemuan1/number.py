# number.py / Python Numbers

x = 30    # int
y = 9.8   # float
z = 20j   # complex
print(type(x)) 
print(type(y)) 
print(type(z)) 

# integer (int) akan memunculkan nilai tanpa koma atau bilangan bulat
x = 1234
y = 914793794
z = -7128394
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# float akan memunculkan nilai bilangan desimal atau koma
a = 3.14
b = -0.001
c = 2.0
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# complex merupakan tipe data bilangan kompleks yang memiliki bagian real dan imajiner
d = 52 + 3j
e = 21j
f = -7.5 + 0j
print(d)
print(e)
print(f)
print(type(d))
print(type(e))
print(type(f))


# konversi tipe data angka
x = 144    # int
y = 9.8    # float
z = 10j    # complex

a = float(x)   # int berubah menjadi float
b = int(y)     # float berubah menjadi int
c = complex(x) # int menjadi complex

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))