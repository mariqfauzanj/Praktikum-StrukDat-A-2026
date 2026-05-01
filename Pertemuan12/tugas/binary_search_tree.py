class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__ (self):
        self.root = None

    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')
            return
        
        current = self.root
        while True:
            if id_buku < current.id_buku:
                if current.left is None:
                    current.left = new_node
                    print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')
                    return
                current = current.left

            elif id_buku > current.id_buku:
                if current.right is None:
                    current.right = new_node
                    print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')
                    return
                current = current.right

            else:
                print(f'[INSERT] Gagal memasukkan: ID {id_buku} sudah ada.')
                return
            
    def search(self, id_buku):
        current = self.root
        while current is not None:
            if id_buku == current.id_buku:
                print(f'[SEARCH] Mencari ID {id_buku}... Ditemukan! Judul:  {current.judul}')
                return
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right

        print(f'[SEARCH] Mencari ID  {id_buku}... Data tidak ditemukan.')

    def get_min(self):
        if self.root is None:
            print('[STATISTIK] Tree kosong. Tidak ada ID terkecil.')

        current = self.root
        while current.left is not None:
            current = current.left
        print(f'[STATISTIK] ID Terkecil: {current.id_buku}')
    
    def get_max(self):
        if self.root is None:
            print('[STATISTIK] Tree kosong. Tidak ada ID terbesar.')

        current = self.root
        while current.right is not None:
            current = current.right
        print(f'[STATISTIK] ID Terbesar: {current.id_buku}')

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1    

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(f'{inorder.counter + 1}. {node.id_buku} - {node.judul}')
        inorder.counter += 1
        inorder(node.right)

inorder.counter = 0

def main():

    bst = BinarySearchTree()
    sep = '=' * 40

    print('SISTEM KATALOG PERPUSTAAKAAN "ILMU TERANG"')
    print(sep)

    # Input data
    bst.insert(50, 'Dasar Pemrograman')
    bst.insert(30, 'Struktur Data')
    bst.insert(70, 'Kecerdasan Buatan')
    bst.insert(20, 'Matematika Diskrit')
    bst.insert(40, 'Basis Data')
    bst.insert(60, 'Jaringan Komputer')
    bst.insert(80, 'Sistem Operasi')

    # Cek koleksi dengan In-Order Traversal
    print('\n[INFO] Koleksi Buku (In-Order Traversal):')
    inorder(bst.root)
    print()

    # Pencarian
    bst.search(60)
    bst.search(100)
    print()

    # Statistik
    bst.get_min()
    bst.get_max()
    print(f'[INFO] Tinggi (Height) Tree: {bst.height(bst.root)}')

    print(sep)
    print('Simulasi Selesai!')

main()