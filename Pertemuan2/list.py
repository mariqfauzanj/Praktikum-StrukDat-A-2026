# 1. beginning
data = ["aku", "kau", "uka", "aku"]
print(data)

# list length
angka = [1, 2, 3]
print(len(angka))

# random fill list allowed
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#type()
data = ["a", "b", "c"]
print(type(data))

# 2. akses list
nihon = ["ichi", "ni", "san"]
print(nihon[1])

# negative indexing
kegiatan = ["saya", "makan", "nasi"]
print(kegiatan[-1])

# range index
keluarga = ["ayah", "bunda", "caca", "saya", "kakak"]
print(keluarga[2:4])
print(keluarga[:4])
print(keluarga[2:])

# range negative indexing
keluarga = ["ayah", "bunda", "caca", "saya", "kakak"]
print(keluarga[-4:-1])

# 3. change item
keluarga = ["ayah", "bunda", "caca"]
keluarga[1] = "saya"
print(keluarga)

# change a range of item
keluarga = ["ayah", "ter", "mul", "saya", "nenek"]
keluarga[1:3] = ["bunda", "caca"]
print(keluarga)

# 4. add list
# append
lirik = ["burung", "kakatua", "hinggap"]
lirik.append("di jendela")
print(lirik)

# inserting
lirik = ["burung", "kakatua", "di jendela"]
lirik.insert(2, "hinggap")
print(lirik)

# extend
lakilaki = ["ayah", "saya"]
perempuan = ["bunda", "caca"]
lakilaki.extend(perempuan)
print(lakilaki)

# 5. remove list
# remove sp. item
makanan = ["eskrim", "rasa", "vanilla"]
makanan.remove("rasa")
print(makanan)

# remove sp. index (pop)
makanan = ["eskrim", "rasa", "vanilla"]
makanan.pop(1)
print(makanan)

# remove sp. index (del)
title = ["19 juta", "lapangan", "basket"]
del title[0]
print(title)

# clear list
pekerjaan = ["pe", "ja", "bat"]
pekerjaan.clear()
print(pekerjaan)