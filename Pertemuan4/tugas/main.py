from tabulate import tabulate
from kurs import kurs, kurs_tampil
from konverter import konversi_uang

def main():
    print('=== KONVERTER MATA UANG ===')

    # tabel data
    tabel_data = []
    for negara in kurs.keys():
       tabel_data.append([negara, kurs_tampil[negara]])

    # tampil tabel
    print(tabulate(tabel_data, headers=['Kode', 'Kurs'], tablefmt='psql'))
    print()

    # input user
    dari = input('Dari (IDR/USD/EUR/SGD/JPY): ').strip().upper()
    ke = input('Ke (IDR/USD/EUR/SGD/JPY): ').strip().upper()

    while True:
        try:
            jumlah = float(input('Jumlah: '))
            break
        
        except ValueError:
            print('Harus berupa angka!')
            continue

    print()

    # konversi IDR ke mata uang lain atau sebaliknya
    if dari == 'IDR':
        hasil = jumlah / kurs[ke]
        format_asal = f"Rp {jumlah:,.0f}".replace(',', '.')
    elif ke == 'IDR':
        hasil = jumlah * kurs[dari]
        format_asal = f"{jumlah:,.2f} {dari}".replace(',', '.')
    else:
        hasil = konversi_uang(jumlah, dari, ke)
        format_asal = f"{jumlah:,.2f} {dari}".replace(',', '.')

    # hasil format
    hasil_format = f"{hasil:,.2f}".replace(',', '.')

    # tampilkan hasil
    print(f"{format_asal} = {hasil_format} {ke}")

main()