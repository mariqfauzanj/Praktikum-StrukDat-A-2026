katalog = [
    {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
    {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}
]

def cari_buku (katalog, keyword):
    for i in range(len(katalog)):
        try:
            daftar = katalog[i]['nama'].lower()
            daftar.index(keyword)
            return i
        
        except ValueError:
            print('Buku tidak ditemukan')

#cari_buku()
