# string.py / Python Strings

# penggunaan kutipan tunggal dan ganda
print('Hapus aku!') # output : Hapus aku!
print("Hapus aku!") # output : Hapus aku!

# penggunaan assignment string ke variabel
nama = "Ariq"
print(nama) # output : Ariq

# multiline string
kebun = """Lihat kebunku, penuh dengan bunga."""
print(kebun) # output : Lihat kebunku, penuh dengan bunga.

bunga = '''Ada melati dan ada yang mawar.'''
print(bunga) # output : Ada melati dan ada yang mawar.

# String array
arrA = "Armada"
print(arrA[4])  # output : a

# Slicing string
b = "Dua tiga empat lima"
print(b[2:3])    # output : a

# Slicing dari start
print(b[:5])     # output : Dua t

# Slicing sampai end
print(b[5:])     # output : tiga empat lima

# Slicing negative index
print(b[-5:-2])  # output : mil

# Looping string
for x in "Ariq":
    print(x)    # output : A r i q

# modifikasi string dengan membentuk uppercase
a = "Minecraft: Also play Terraria!"
print(a.upper()) # output :  MINECRAFT: ALSO PLAY TERRARIA!

# modifikasi string dengan membentuk lowercase
x = "Minecraft: Also play Stardew Valley!"
print(x.lower()) # output :  minecraft: also play stardew valley!

# menghapus whitespace pada string
g = "   Minecraft: Use mods!  "
print(g.strip()) # output : Minecraft: Use mods!

# mengganti karakter pada string
y = "Lebahan dulu."
print(y.replace("L", "R")) # output : Rebahan dulu.

# memecah string menjadi array
z = "Dia, Kamu, Kalian,,"
print(z.split(",")) # output : ['Dia', ' Kamu', ' Kalian', '', '']

# penggabungan string (concat)
p = "Halo,"
q = "saya"
r = p + " " + q + " Ariq."
print(r) # output : Halo, saya Ariq.

# F-string
umur = 19
pesan = f"Saya Ariq, saya berumur {umur} tahun."
print(pesan) # output : Saya Ariq, saya berumur 19 tahun.

# Placeholder
harga = 5
pesan = f"Harga dompet di Amerika sekitar {harga:.2f} dollar US."
print(pesan) # output : Harga dompet di Amerika sekitar 5.00 dollar US.

# Placeholder (dengan operasi matematika)
pesan = f"Harga pesanan sekitar {20 * 5} dollar"
print(pesan ) # output : Harga pesanan sekitar 100 dollar

# escape character
text = "Ibu berkata, \"Jangan pulang kemalaman!\""
print(text) # output : Ibu berkata, "Jangan pulang kemalaman!"