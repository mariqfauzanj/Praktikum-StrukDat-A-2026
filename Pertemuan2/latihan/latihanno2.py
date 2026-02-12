# no.2

dosen = ("D001", "Dr. Andi", "Struktur Data", 12)

print("Nama dosen: ", dosen[1])
print("Mata kuliah: ", dosen[2])
print("SKS: ", dosen[3]) # sebelum diganti

dosen2 = list(dosen)
dosen2[3] = "14"

dosen = tuple(dosen2)

print("SKS: ", dosen[3]) # setelah diganti
print(dosen)

# SKS berubah menjadi 14 pada saat menggunakan method list(dosen) pada variabel dosen2 dan tuple(dosen) pada variabel dosen2
# Kelebihan: Tuple berurutan dan tidak tergantikan (unchangeable)