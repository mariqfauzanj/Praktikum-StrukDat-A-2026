from analisis import analisis_toko_buku, buku

def tampilkan_analisis_toko(data_buku):
    hasil = analisis_toko_buku(data_buku)
    if not hasil:
        return
    
    print('=== LAPORAN TOKO BUKU ===')
    print(f"Total Buku          : {hasil['total_buku']}")
    print(f"Kategori Terbanyak  : {hasil['kategori_terbanyak']}")
    print(f"Rata-rata Harga     : Rp {hasil['rata_harga']*1000:,.0f}")
    print(f"Buku Termurah       : {hasil['buku_termurah']}")
    print(f"Tahun Terbaru       : {hasil['tahun_terbaru']}")
    print('=' * 10)

#tampilkan_analisis_toko(buku)