class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Menambah node di akhir
    def append(self, data):
        new_node = Node(data)

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

    # Menambah node di awal
    def prepend(self, data):
        new_node = Node(data)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        # Cari node terakhir
        while current.next != self.head:
            current = current.next

        # Node baru menunjuk ke head lama
        new_node.next = self.head

        # Node terakhir menunjuk ke head baru
        current.next = new_node

        # Pindahkan head
        self.head = new_node

    # Menghapus node berdasarkan data
    def delete(self, data):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            # Jika node ditemukan
            if current.data == data:
                
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

    # Menampilkan linked list
    def display(self):
        if self.head is None:
            print("Linked list kosong")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(kembali ke head)")


# Contoh penggunaan
cll = CircularLinkedList()

cll.append(10)
cll.append(20)
cll.append(30)

print("Awal:")
cll.display()

cll.prepend(5)

print("Setelah prepend 5:")
cll.display()

cll.delete(20)

print("Setelah delete 20:")
cll.display()