import soal2

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    pencarian = soal2.cari_buku[katalog, nama_buku]
    
    if katalog[pencarian]['stok'] == 0:
        return 'Stok tidak mencukupi'
    
    if katalog[pencarian]['buku'] == 0:
        return 'Buku tidak ditemukan'
    
    if pencarian and katalog[pencarian]['stok']:
        pr_bayar = jumlah_beli * katalog[pencarian]['harga']
        katalog[pencarian]['stok'] -= jumlah_beli
        print(f'Total Pembayaran: {pr_bayar}')
        return pr_bayar