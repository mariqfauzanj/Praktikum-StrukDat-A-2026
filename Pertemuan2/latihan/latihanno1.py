# no.1

nilai = [75, 80, 65, 90, 85]

nilai.append(95)
nilai.remove(65)
nilai.sort()

n = len(nilai)
jumlah = 0

for i in nilai:
    jumlah+=i

rata = jumlah / n

print ("Urutan: ", nilai)
print ("Max: ", max(nilai))
print ("Min: ", min(nilai))
print("Jumlah data: ", n)
print("Rata-rata: ", rata)