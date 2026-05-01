class plat:
    def __init__(self, data):
        self.data = data
        self.next = None

# Mencari plat_target dalam antrean, lalu menyisipkan plat_baru tepat setelahnya.
def sisipkan_vip(plat_baru, plat_target):
    if plat_target is None:
        return plat_baru
    plat_baru.next = plat_target.next
    plat_target.next = plat_baru
    return plat_target

# Buat fungsi tampilkan_antrean() untuk menunjukkan urutan kendaraan dari depan ke belakang.
def tampilkan_antrean(antrean):
    platIni = antrean
    while platIni:
        print(platIni.data, end=", ")
        platIni = platIni.next
        print()

plat1 = plat("B 1234 ABC")
plat2 = plat("D 8888 XYZ")
plat3 = plat("A 111 TUV")
plat4 = plat("B 2022 EFG")

plat1.next = plat2
plat2.next = plat3
plat3.next = plat4

print("Kendaraan saat ini:")
sisipkan_vip(plat4, plat2)  

plat1 = tampilkan_antrean(plat1, plat3)

print("\nKendaraan yang VIP:")
tampilkan_antrean(plat1)