from analisis import buku

def analisis_per_kategori(data_buku, kategori):
    terfilter = [b for b in data_buku if b['kategori'] == kategori]
    if not terfilter:
        return {}
    
    jumlah = len(terfilter)
    rata_harga = round(sum(b['harga'] for b in terfilter) / jumlah, 1)

    termurah = min(terfilter, key=lambda x: x['harga'])
    termahal = max(terfilter, key=lambda x: x['harga'])

    return {
        'jumlah' : jumlah,
        'rata_harga' : rata_harga,
        'judul_termurah' : termurah['judul'],
        'judul_termahal' : termahal['judul']
    }

print(analisis_per_kategori(buku, "Fiksi"))