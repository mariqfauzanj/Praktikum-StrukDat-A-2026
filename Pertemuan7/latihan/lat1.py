plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

def ganjilgenap(plat):
    ganjil = []
    genap = []
    for p in plat:
        nomor = p.split()[1]
        if int(nomor) % 2 != 0:
            ganjil.append(p)
        else:
            genap.append(p)
    return ganjil, genap

ganjil, genap = ganjilgenap(plat)
print("Ganjil:", ganjil)
print("Genap :", genap)