from analisis import buku

def ranking_buku_termurah(data_buku, n=3):
    if n < 1:
        return []
    
    # Urutkan berdasarkan harga, ambil n pertama
    sorted_buku = sorted(data_buku, key=lambda x: x["harga"])
    top_n = sorted_buku[:n]
    
    return [(b["judul"], b["penulis"], b["harga"]) for b in top_n]


# Tes
print(ranking_buku_termurah(buku, 3))
# [
#   ('One Piece 98', 'Eiichiro Oda', 45),
#   ('Dilan 1990', 'Pidi Baiq', 75),
#   ('Laskar Pelangi', 'Andrea Hirata', 85)
# ]