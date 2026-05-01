'''
Nama: Muhammad Ariq Fauzan J
NIM: 25071206991
Kelas: TI-A
'''

# Struktur Node penyimpan data pasien dan pointer
class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

# Struktur Queue untuk antrian pasien
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    # Enqueue
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return print(f'[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})')

    # Dequeue
    def dequeue(self):
        if self.is_empty():
            return None
        
        removed_node = self.head
        self.head = self.head.next
        removed_node.next = None
        self._size -= 1
        if self.is_empty():
            self.tail = None
        return removed_node

    def peek(self):
        if self.is_empty():
            return None
        return print(f'[PEEK] Pasien berikutnya: {self.head.nama} - {self.head.keluhan}')

    def size(self):
        return print(f'\n[INFO] Jumlah pasien menunggu: {self._size} orang')

    def clear(self):
        while not self.is_empty():
            self.dequeue()
        return print(f'\n[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.')

# ============================ #

def main():
    separator = '=' * 36

    print(separator)
    print('  SISTEM ANTRIAN POLI UMUM')
    print('  RS Sehat Bersama')
    print(separator)

    antrian = Queue()
    
    def pasien_dequeue():
        pasien = antrian.dequeue()
        if pasien:
            print(f'\n[PANGGIL] Dokter memanggil: {pasien.nama} (keluhan: {pasien.keluhan})')
        return pasien

    # cek kondisi awal antrian
    print(f'\n[CEK] Apakah antrian kosong? → {"YA, antrian masih kosong." if antrian.is_empty() else "TIDAK"}\n')
    
    antrian.enqueue('Budi', 'demam tinggi') # daftar pasien ke-1
    antrian.enqueue('Ani', 'batuk pilek') # daftar pasien ke-2
    antrian.enqueue('Citra', 'sakit kepala') # daftar pasien ke-3

    antrian.size() # info/cek jumlah pasien menunggu
    antrian.peek() # cek pasien berikutnya yang akan dipanggil

    pasien_dequeue() # panggil pasien berikutnya, dengan menghapus dari antrian
    antrian.enqueue('Dodi', 'nyeri perut') # daftar pasien ke-4


    print(f'\n[ANTRIAN SAAT INI]') # tampilan daftar antrian saat ini
    current = antrian.head
    pos = 1
    while current:
        print(f'{pos}. {current.nama.ljust(10)} → {current.keluhan}')
        current = current.next
        pos += 1

    pasien_dequeue() # panggil pasien berikutnya, dengan menghapus dari antrian
    antrian.size() # info/cek jumlah pasien menunggu

    antrian.clear() # pengosongan antrian setelah sesi selesai

    # cek antrian sudah kosong atau belum setelah sesi selesai
    print(f'[CEK] Apakah antrian kosong? → {"YA, antrian sudah kosong." if antrian.is_empty() else "TIDAK"}\n')

    print(separator)
    print('  Simulasi Selesai!')
    print(separator)

main()