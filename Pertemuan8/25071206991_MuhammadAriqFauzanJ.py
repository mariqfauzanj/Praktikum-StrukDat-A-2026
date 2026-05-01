# Nama : Muhammad Ariq Fauzan Jatmika
# NIM : 25071206991

# Sistem Antrian Peminjaman Perpustakaan

pengunjung_hari_ini = [
    {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
    "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
    "kembali": True},
    {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
    "kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
    "kembali": True},
    {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
    "kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
    "kembali": False},
]

# 1. list dan dictionary

def tampilkan_pengunjung(): 
    '''Tampilkan semua data pengunjung dalam format tabel.'''

    # bentuk tabel dan sorting nama A-Z
    print('===== DATA PENGUNJUNG PERPUSTAKAAN =====')
    print('No | ID | Nama | Usia | Kategori | Status Kembali')
    print('-' * 42)

    for i, pengunjung in enumerate(pengunjung_hari_ini, start=1):
        print(f'{i} | {pengunjung['id']} | {pengunjung['nama'].ljust(6)} | {pengunjung['usia']} | {pengunjung['kategori']} | {"Sudah Kembali" if pengunjung['kembali'] else "Belum Kembali"}')

def filter_belum_kembali():
    '''Kembalikan list berisi nama-nama pengunjung yang belum mengembalikan buku, 
    lalu tampilkan total jumlah mereka.'''

    # list comprehension
    belum_kembali = [p for p in pengunjung_hari_ini if not p['kembali']]

    # list nama yang belum kembali
    print('\n===== PENGUNJUNG BELUM KEMBALI =====')

    # sort A-Z
    belum_kembali.sort(key=lambda x: x['nama'])
    for i, pengunjung in enumerate(belum_kembali, start=1):
        print(f'{i}. {pengunjung['nama']}')
    print(f'Total belum kembali: {len(belum_kembali)} pengunjung')

tampilkan_pengunjung()
filter_belum_kembali()

print()

# 2. tuple dan set

def info_perpustakaan():
    '''Kembalikan informasi tetap perpustakaan menggunakan tuple lalu tampilkan isinya.'''
    
    print('''Info Perpustakaan:
Nama   : Perpustakaan Kampus Terpadu
Alamat : Jl. Pendidikan No. 5, Pekanbaru
Telp   : 0761-54321
''')

def rekap_kategori():
    '''Menggunakan set untuk mendapatkan kategori buku unik, lalu hitung jumlah pengunjung per kategori menggunakan dictionary.'''
    kategori_buku_unik = set(p['kategori'] for p in pengunjung_hari_ini)
    jumlah_kategori = len(kategori_buku_unik)

    print(f'Kategori Buku Unik: {kategori_buku_unik}')
    print(f'Jumlah kategori: {jumlah_kategori}\n')

    print('Rekap per kategori:')
    for kategori in kategori_buku_unik:
        jumlah = sum(1 for p in pengunjung_hari_ini if p['kategori'] == kategori)
        print(f'{kategori}: {jumlah} pengunjung')
    
    # Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung)
    print(f'\nKategori terbanyak: {kategori_buku_unik} ({sum(1 for p in pengunjung_hari_ini if p['kategori'] == kategori)} pengunjung)')

info_perpustakaan()
rekap_kategori()


# 3. OOP
class Pengunjung:
    '''
    - Atribut private: __id, __nama, __kategori
    - Getter untuk setiap atribut
    - Method tampilkan_info()
    - Method static hitung_pengunjung() -> mengembalikan total objek
      Pengunjung yang sudah dibuat (gunakan class variable sebagai counter)
    '''
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori

    # getter atribut private
    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):
        print(f'\nID        : {self.__id}\nNama      : {self.__nama}\nKategori  : {self.__kategori}')

    # metode statis menghitung pengunjung
    total_pengunjung = 0
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.total_pengunjung += 1
    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.total_pengunjung
    
class PengunjungPrioritas(Pengunjung):
    '''
    - Tambahkan atribut: prioritas ("Mendesak" / "Biasa")
    - Override tampilkan_info() untuk menyertakan info prioritas
    - Jika prioritas = "Mendesak", tampilkan pesan peringatan:
    "** Layani segera! **"
    '''
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f'Prioritas : {self.prioritas}')
        if self.prioritas == "Mendesak":
            print('** Layani segera! **\n')


antre1 = Pengunjung('M001', 'Rina', 'Fiksi')
antre2 = PengunjungPrioritas('M007', 'Gilang', 'Referensi', 'Mendesak')
antre1.tampilkan_info()
antre2.tampilkan_info()
print('Total pengunjung terdaftar: ', Pengunjung.hitung_pengunjung())

print()

# 4. Single linked list
'''
Perpustakaan menggunakan Single Linked List untuk mengatur antrian layanan petugas.
Pengunjung yang datang lebih awal akan dilayani lebih dulu (FIFO).
'''

class Node:
    '''
    - data : dictionary {"id", "nama", "kategori"}
    - next : pointer ke node berikutnya
    '''
    def __init (self, data):
        self.data = data
        self.next = None

class AntrianPeminjaman:
    '''
    - head : node pertama
    - tambah(data) -> tambah pengunjung di akhir antrian
    - tampilkan() -> tampilkan seluruh antrian beserta posisinya
    - panggil_berikutnya() -> hapus dan tampilkan pengunjung paling depan
    - cari(nama) -> cari pengunjung berdasarkan nama, tampilkan
    posisinya
    - hapus_berdasarkan_id(id) -> hapus pengunjung berdasarkan ID
    di mana saja posisinya dalam antrian
    - hitung() -> kembalikan jumlah pengunjung dalam antrian
    '''
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_Node
    
    def tampilkan(self):
        current = self.head
        print('===== ANTRIAN PEMINJAMAN =====')
        posisi = 1
        while current:
            print(f'[{posisi + 1}] {current.data["id"]} - {current.data["nama"].ljust(6)} | {current.data["kategori"]}')
            current = current.next
            posisi += 1
        print('Total antrian: ', posisi - 1)

    def panggil_berikutnya(self):
        if self.head is not None:
            dipanggil = self.head.data
            self.head = self.head.next
            print('Memanggil pengunjung berikutnya...')
            
    def cari(self.nama):
        current = self.head
        posisi = 1
        while current:
            if current.data['nama'] == nama:
                print(f'Silahkan masuk: {current.data["nama"]} [{current.data["id"]}] - {current.data["kategori"]} (Posisi: {posisi})')
                return
            current = current.next
            posisi += 1
        else:
            return None
        
    def hapus_berdasarkan_id(self, id):
        current = self.head
        prev = None
        print(f'Menghapus pengunjung dengan ID {id}...')
        while current:
            if current.data['id'] == id:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                print(f'{current.data["nama"]} [{id}] telah dihapus dari antrian.')
                return
            prev = current
            current = current.next
            
antrian = AntrianPeminjaman()
antrian.tambah({"id": "M001", "nama": "Rina", "kategori": "Fiksi"})
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})

antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("M003")
antrian.tampilkan()
antrian.cari("Taufik")
print("Total antrian:", antrian.hitung())