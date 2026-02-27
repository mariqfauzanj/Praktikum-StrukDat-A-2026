from kurs import kurs

def konversi_uang(jumlah, dari, ke):
    # konversi jumlah dari mata uang 'dari' ke mata uang 'ke'
    if dari not in kurs or ke not in kurs:
        return None # mata uang tidak dikenal
    
    # step 1, ke IDR
    jumlah_idr = jumlah * kurs[dari]

    # step 2, dari IDR ke mata uang lain
    hasil = jumlah_idr / kurs[ke]

    return hasil