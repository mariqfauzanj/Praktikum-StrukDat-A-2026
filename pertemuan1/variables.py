# variables.py / Python Variables

# membuat variabel dan memberikan nilai
x = 2026
y = "Juli"
print(x)        # output : 2026
print(y)        # output : Juli
print(y, x)     # output : Juli 2026


# variabel dapat berubah tipe data
p = 45          # x merupakan int
p = "Pekanbaru" # x menjadi str
print(p)        # output : Pekanbaru

x = str(90)    # ini merupakan string
y = int(47)    # ini merupakan integer
print(x)      # output : '90'
print(y)      # output : 47


# penamaan variabel dengan tiga gaya
peluruDalamMagazine = 30   # ini merupakan camel case
umur_senjata_saya = 25     # ini merupakan snake case
NamaPanggilanSaya = "Ariq" # ini merupakan pascal case

print(peluruDalamMagazine) # output : 30
print(umur_senjata_saya)   # output : 25
print(NamaPanggilanSaya)   # output : Ariq

# penamaan variabel yang salah
"""
6767variabel = "Dewa" (angka tidak boleh ada di depan kalimat)
satu-variabel = "Dewi" (tidak boleh ada simbol selain underscore)
ini python = "Sutejo" (tidak boleh ada spasi di dalam variabel)
"""

# banyak value ke dalam beberapa variabel
a, b, c = 26, 2006, "Juli"

print(a) # output : 26
print(b) # output : 2006
print(c) # output : Juli
print (a, c, b) # output : 26 Juli 2006


# satu value ke dalam beberapa variabel
p = q = r = "250"
print(p) # output : 250
print(q) # output : 250
print(r) # output : 250
print (p, q, r) # output : 250 250 250


# unpacking variabel
peluru = ["9mm", "5.56mm", "7.62mm"]
x, y, z = peluru
print(x) # output : 9mm
print(y) # output : 5.56mm
print(z) # output : 7.62mm
print (x, y, z) # output : 9mm 5.56mm 7.62mm


# Output variabel seperti berikut
nama = "Ariq"
umur = 19
print("Nama saya " + nama + ", umur saya " + str(umur) + " tahun.") # output : Nama saya Ariq, umur saya 19 tahun.

m = "Saya "
n = "belajar "
o = "Python."
print(m + n + o) # output : Saya belajar Python.