'''
Toko buku "Literasi" ingin mencatat daftar buku (judul & pengarang)
menggunakan Double Linked List agar bisa ditelusuri dari depan maupun belakang.
'''

# class Node dengan atribut judul, pengarang, prev, dan next.
class Node:
    def __init__ (self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

# Buat fungsi insert_tail(), lalu tambahkan buku: Laskar Pelangi, Bumi Manusia, dan Sang Pemimpi.
class DLLLiterasi:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            return
        
        # Cari node terakhir
        current = self.head
        while current.next:
            current = current.next

        # Hubungkan node terakhir dengan node baru
        current.next = new_node
        new_node.prev = current

    # Buat fungsi print_forward() dan print_backward(), lalu jalankan keduanya.
    def print_forward(self):
        current = self.head
        while current is not None:
            print(f'{current.judul}, {current.pengarang}', end=' <-> ')
            current = current.next
        print("None")
    
    def print_backward(self):
        current = self.head
        if current is None:
            return
        
        # Pindah ke node terakhir
        while current.next:
            current = current.next
        
        # Tampilkan dari belakang ke depan
        while current is not None:
            print(f'{current.judul}, {current.pengarang}', end=' <-> ')
            current = current.prev
        print("None")


    # Buat fungsi delete_by_judul(), hapus buku "Bumi Manusia", lalu tampilkan list kembali.
    def delete_by_judul(self, judul):
        current = self.head

        while current:
            if current.judul == judul:
                # Jika node pertama
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                  # Menghubungkan node sebelumnya dengan node berikutnya
                    current.prev.next = current.next

                    if current.next:
                      # Menghubungkan node berikutnya dengan node sebelumnya
                        current.next.prev = current.prev
                return

            current = current.next

dll = DLLLiterasi()

dll.insert_tail('Laskar Pelangi', 'Andrea Hirata')
dll.insert_tail('Bumi Manusia', 'Tere Liye')
dll.insert_tail('Sang Pemimpi', 'Andrea Hirata')

print("\nForward:")
dll.print_forward()

print("\nBackward:")
dll.print_backward()

dll.delete_by_judul('\nHapus by judul:')

print("\nSetelah hapus:")
dll.print_forward()