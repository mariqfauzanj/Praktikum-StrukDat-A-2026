level_diskon = (
    (500000, 15), # belanja >= 500.000 -> diskon 15%
    (300000, 10), # belanja >= 300.000 -> diskon 10%
    (100000, 5), # belanja >= 100.000 -> diskon 5%
    (0, 0), # default -> tidak ada diskon
)

def hitung_diskon(total_belanja, level_diskon, index=0):
    #menampilkan diskon dengan harga
    print('=== Diskon ===')
    for i in range(len(level_diskon) - 1):
        print(f'{i+1}. Diskon {level_diskon[i]}% dalam pembelian seharga Rp {level_diskon[index]}')

    '''
    if total_belanja >= level_diskon[index][0]:
        hitung = total_belanja * level_diskon[index][1]
        hasil = hitung - total_belanja
    
    else:
        print('Tidak ada diskon')
    '''