class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Menambah node di akhir
    def append(self, data):
        new_node = Node(data)

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

    # Menambah node di awal
    def prepend(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    # Menghapus node berdasarkan data
    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
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

    # Menampilkan dari depan ke belakang
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Menampilkan dari belakang ke depan
    def display_backward(self):
        current = self.head

        # Pergi ke node terakhir
        while current and current.next:
            current = current.next

        # Tampilkan mundur
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Contoh penggunaan
dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)

dll.prepend(5)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()

dll.delete(20)

print("Setelah hapus 20:")
dll.display_forward()