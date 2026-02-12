class Person:
    def __init__(self, nama, tinggi, umur):
        self.nama = nama
        self.tinggi = tinggi
        self.umur = umur

class Karyawan(Person):
    def __init__(self, nama, tinggi, umur, gaji):
        super().__init__(nama, tinggi, umur)
        self._gaji = gaji

    def get_gaji(self):
        return self._gaji

class Rekening:
    def __init__(self, norek):
        self.norek = norek
        self.__PIN = ""

    def set_PIN(self, PIN):
            if PIN > 8:
                self._PIN = PIN
            else:
                print("PIN harus terdiri dari 8 karakter")
        
    def get_PIN(self):
            return self.__PIN


p1 = Person("Riki", 170, 20)
print(p1.nama)

p2 = Karyawan("Riki", 170, 20, 4000000)
print(p2.get_gaji())

p3 = Rekening(13243546)
p3.set_PIN(1234567)
p3.get_PIN()