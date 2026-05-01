class plat:
    def __init__(self, data):
        self.data = data
        self.next = None

def tambahKendaraan(plat):
  platIni = plat
  while platIni:
    print(platIni.data, end=", ")
    platIni = platIni.next
  print()


def hapusKendaraan(plat, platDihapus):
    if plat == platDihapus:
        return plat.next

    platIni = plat
    while platIni.next and platIni.next != platDihapus:
        platIni = platIni.next
    if platIni.next is None:
        return plat
    platIni.next = platIni.next.next
    return plat

plat1 = plat("B 1234 ABC")
plat2 = plat("D 8888 XYZ")
plat3 = plat("A 111 TUV")
plat4 = plat("B 2022 EFG")

plat1.next = plat2
plat2.next = plat3
plat3.next = plat4

print("Kendaraan saat ini:")
tambahKendaraan(plat1)

plat1 = hapusKendaraan(plat1, plat3)

print("\nKendaraan yang tidak mogok saat ini:")
tambahKendaraan(plat1)