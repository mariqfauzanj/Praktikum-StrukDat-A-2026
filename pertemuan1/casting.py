# casting.py / Python Type Casting

'''
pada integer dapat membangun bilangan bulat dari bilangan itu sendiri, 
bilangan pecahan (dengan menghilangkan semua desimal),
atau string (tersebut mewakili bilangan bulat).
'''
a = int(12)
b = int(9.8)
c = int("36")
print(a)      # output : 12
print(b)      # output : 9
print(c)      # output : 36

'''
pada float dapat membangun bilangan desimal dari bilangan itu sendiri, 
bilangan bulat (dengan menambahkan .0 di belakang bilangan bulat), 
atau string (tersebut mewakili bilangan desimal).
'''

p = float(100)
q = float(23.1)
r = float("314")
print(p)      # output : 100.0
print(q)      # output : 23.1
print(r)      # output : 314.0

'''
pada string dapat membangun string dari bilangan bulat,
bilangan desimal, atau string itu sendiri.
'''

x = str(459)
y = str(12.96)
z = str("Hello, my friend! Ini adalah string.")
print(x)      # output : '459'
print(y)      # output : '12.96'
print(z)      # output : 'Hello, my friend! Ini adalah string.'