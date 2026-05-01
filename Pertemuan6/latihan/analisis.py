def analisis_toko_buku(data_buku):
    if not data_buku:
        return {}
    
    total_buku = len(data_buku)

    #hitung jumlah per kat.
    kategori_count = {}
    for item in data_buku:
        kat = item['kategori']
        kategori_count[kat] = kategori_count.get(kat, 0) + 1

    kategori_terbanyak = max(kategori_count, key=kategori_count.get)

    #rata2 harga
    total_harga = sum(item['harga'] for item in data_buku)
    rata_harga = round(total_harga / total_buku, 1)
        
    #buku termurah
    buku_termurah = min(data_buku, key=lambda x: x['harga'])
    judul_termurah = buku_termurah['judul']

    #thn terbaru
    tahun_terbaru = max(item['tahun'] for item in data_buku)

    return {
    "total_buku": total_buku,
    "kategori_terbanyak": kategori_terbanyak,
    "rata_harga": rata_harga ,
    "buku_termurah": judul_termurah,
    "tahun_terbaru": tahun_terbaru
    }

#diketahui
buku = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005, "harga": 85, "kategori": "Fiksi"},
    {"judul": "Bumi Manusia", "penulis": "Pramoedya Ananta Toer", "tahun": 1980, "harga": 120, "kategori": "Fiksi"},
    {"judul": "Matematika SMA X", "penulis": "Tim Erlangga", "tahun": 2023, "harga": 195, "kategori": "Pelajaran"},
    {"judul": "One Piece 98", "penulis": "Eiichiro Oda", "tahun": 2022, "harga": 45, "kategori": "Komik"},
    {"judul": "Sapiens", "penulis": "Yuval Noah Harari", "tahun": 2011, "harga": 180, "kategori": "Nonfiksi"},
    {"judul": "Dilan 1990", "penulis": "Pidi Baiq", "tahun": 2014, "harga": 75, "kategori": "Fiksi"}
]

#hasil = analisis_toko_buku(buku)
#print(hasil)