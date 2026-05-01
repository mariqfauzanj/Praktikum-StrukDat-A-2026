from analisis import buku

def info_unik_buku(data_buku):
    penulis_unik = {b['penulis'] for b in data_buku}
    kategori_unik = {b['kategori'] for b in data_buku}
    tahun_set = {b['tahun'] for b in data_buku}

    return (
        len(penulis_unik),
        kategori_unik,
        tahun_set
    )

#print(info_unik_buku(buku))