from analisis import buku

def diskon_per_kategori(data_buku, kategori, persen):
    if persen < 0 or persen > 100:
        return data_buku[:]  # kembalikan copy asli jika persen salah
    
    faktor = (100 - persen) / 100
    hasil = []
    
    for buku in data_buku:
        buku_baru = buku.copy()
        if buku_baru["kategori"] == kategori:
            buku_baru["harga"] = round(buku_baru["harga"] * faktor)
        hasil.append(buku_baru)
    
    return hasil


# Contoh: diskon 20% untuk semua buku Fiksi
hasil_diskon = diskon_per_kategori(buku, "Fiksi", 20)
for b in hasil_diskon:
    print(f"{b['judul']}: Rp {b['harga']*1000:,}")