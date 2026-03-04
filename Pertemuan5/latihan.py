#1
stok_barang = [15, 40, 30, 10, 25]
print('Soal stok Barang')

# a. Temukan indeks dari nilai 10, lalu ubah nilai pada indeks tersebut menjadi 50.
ind10 = stok_barang.index(10)
stok_barang[ind10] = 50
print(stok_barang)

# b. Tambahkan nilai 5 ke akhir list, 
# kemudian urutkan list secara descending (besar ke kecil).
stok_barang.append(5)
stok_barang.sort(reverse=True)
print(stok_barang)

# c. Tampilkan jumlah total seluruh nilai dalam list tersebut.
total_stok = sum(stok_barang)
print(total_stok)

# d. Gunakan shorthand if (ternary) untuk menampilkan "Stok Aman" jika rata-rata nilai
# dalam list > 20, jika tidak tampilkan "Waspada".
rata_stok = total_stok / len(stok_barang)
status = "Aman" if rata_stok > 20 else 'Waspada'
print(status)

#2
print('Predikat Mahasigma')
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for nama, nilai in data_aktivitas:
    if nilai > 80:
        print(f'{nama} mendapatkan predikat Gold')
    elif nilai < 50:
        print(f'{nama} mendapatkan predikat Bronze')
    else:
        print(f'{nama} mendapatkan predikat Silver')

#3
print('UKM Coding dan Robotik')
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

# a. mahasigma yang hanya mendaftar di ukm_coding saja
just_coding = ukm_coding - ukm_robotik
print('Mahasigma hanya coding: ', just_coding)

# b. seluruh mahasigma unik yang mendaftar di salah satu atau keduanya
unik_mhs = ukm_coding | ukm_robotik
print('Mahasigma terunik: ', unik_mhs)

# c. Cek apakah "Andi" merupakan anggota dari ukm_robotik.
if 'Andi' in ukm_robotik:
    print('Andi BUKAN anggota UKM Robotik')

#4
print('Gudang PC')
gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
]

# a. Tambah key baru bernama "kategori" dengan nilai "Aksesoris" untuk produk Keyboard.
for produk in gudang_pc:
    if produk['item'] == 'Keyboard':
        produk['Kategori'] = 'Aksesoris'

# b. Tambahkan satu item baru: "Headset" dengan harga 350000 dan stok 8.
gudang_pc.append({'item': 'Headset', 'harga': 350000, 'stok': 8})

# c. Hitung Total Nilai Aset (Harga x Stok) untuk setiap item.
# Output: Item: [Nama] | Total Aset: Rp [Hasil Perkalian]
for produk in gudang_pc:
    aset = produk['harga'] * produk['stok']
    print(f'Item: {produk['item']} | Total Aset: Rp {aset}')