class HashLibrary:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, kode):
        total = 0
        for char in str(kode):
            total += ord(char)
        return total % self.size
    
    def insert(self, kode, judul):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == kode:
                bucket[i] = (kode, judul)
                print(f'\nBuku {kode} "{judul}" berhasil di-update.')
                return
        bucket.append((kode, judul))
        print(f'\nBuku {kode} "{judul}" berhasil ditambahkan.')

    def search(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for k, v in bucket:
            if k == kode:
                print(f'\nBuku ditemukan: {kode} - {v}')
                return
        print(f'\nBuku dengan kode {kode} tidak ditemukan.')

    def delete(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == kode:
                del bucket[i]
                print(f'\nBuku {kode} "{v}" berhasil dihapus.')
                return
        print(f'\nBuku dengan kode {kode} tidak ditemukan.')

    def display(self):
        print("\nIsi rak buku :")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f'Buku ke-{i}:')
                for k, v in bucket:
                    print(f'{k} - {v}')

def main():
    lib = HashLibrary()

    lib.insert("BK111", "Mahir C++ Dalam Satu Jam")
    lib.insert("BK222", "Python Dasar")
    lib.insert("BK333", "Matematika Diskrit")
    lib.insert("BK444", "Atomic Habits")
    lib.insert("BK555", "Bob si Kuli")
    lib.insert("BK999", "0x037791e")

    lib.display()

    lib.insert("BK045", "Mein Kampf")
    lib.insert("BK046", "Book of Mussolini")
    lib.insert("BK046", "How to be a Dictator")
    lib.insert("BK088", "How to ride Tiger I")
    lib.insert("BK111", "Bumi Manusia")

    lib.display()

    lib.search("BK045")
    lib.search("BK050")

    lib.delete("BK046")

    lib.display()

main()