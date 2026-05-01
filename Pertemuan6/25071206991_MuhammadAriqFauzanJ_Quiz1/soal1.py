def tambah_buku(nama = str, harga = float, stok = int):
    buku = dict()

    if (harga or stok) <= 0:
        print('Error!')
        return None
    buku.update({'nama': nama, 'harga': harga, 'stok': stok})

    return buku
    

semua_buku = []
for i in range(3):
    nama = [str(input(f'Nama buku ke-{i+1} : '))]
    harga = [float(input(f'Harga buku ke-{i+1}: '))]
    stok = [int(input(f'Stok buku ke-{i+1} : '))]
    semua_buku.append(tambah_buku(*nama, *harga, *stok))

print(semua_buku)
