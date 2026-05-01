'''
Kasir toko menggunakan Circular Linked List untuk antrian pelanggan. Antrian
awal: Andi → Budi → Citra → Dina → (kembali ke Andi).
'''
# Buat class Node dengan atribut nama dan next. Buat fungsi insert_tail() dan tambahkan 4 pelanggan.
class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class Kasir:
    def __init__(self):
        self.head = None
        
    def insert_tail(self, nama):
        new_node = Node(nama)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        # Cari node terakhir
        while current.next != self.head:
            current = current.next

        # Sambungkan node terakhir ke node baru
        current.next = new_node
        new_node.next = self.head

    def print_antrian(self):
        if self.head is None:
            print("Antrian kosong.")
            return

        current = self.head

        while True:
            print(current.nama, end=" → ")
            current = current.next
            if current == self.head:
                break
        print("(kembali ke {})".format(self.head.nama))

    # Tambahkan pelanggan baru Edo di akhir antrian menggunakan insert_tail(), lalu tampilkan antrian.
    def tambah_pelanggan(self, nama):
        self.insert_tail(nama)

# Buat fungsi delete_head(), hapus Andi (sudah dilayani), lalu tampilkan antrian.
    def delete_head(self, nama):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            # Jika node ditemukan
            if current.nama == nama:
                
                # Jika hanya ada 1 node
                if current == self.head and current.next == self.head:
                    self.head = None
                    
                # Jika menghapus head
                elif current == self.head:
                    last = self.head
                    
                    # Cari node terakhir
                    while last.next != self.head:
                        last = last.next
                        
                    # Head pindah ke node berikutnya
                    self.head = self.head.next
                    
                    # Node terakhir menunjuk ke head baru
                    last.next = self.head
                    
                # Jika menghapus node biasa / terakhir
                else:
                    
                # 10 (prev) -> 20 (current) -> 30 (current.next)
                    prev.next = current.next

                return

            # Geser ke node berikutnya (prev = None, current = 10) -> (prev = 10, current = 20) -> (prev = 20, current = 30)
            prev = current
            current = current.next

            # Jika sudah kembali ke head, berarti data tidak ada
            if current == self.head:
                break

kasir = Kasir()
kasir.insert_tail("Andi")
kasir.insert_tail("Budi")
kasir.insert_tail("Citra")
kasir.insert_tail("Dina")
kasir.print_antrian()
kasir.delete_head("Andi")
kasir.print_antrian()