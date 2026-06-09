class HashTable:

    # =========================================
    # Membuat hash table dengan 10 bucket
    # Setiap bucket berupa list kosong
    # =========================================
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    # =========================================
    # Hash Function
    # Mengubah key menjadi index bucket
    # Langkah:
    # 1. Ambil Unicode tiap karakter
    # 2. Jumlahkan
    # 3. Modulo dengan ukuran table/array
    # =========================================
    def hash_function(self, key):
        total = 0

        # Jumlahkan Unicode tiap karakter
        for char in str(key):
            total += ord(char)

        return total % self.size

    # =========================================
    # Insert Function
    # Menambahkan pasangan key:value
    #
    # Jika key sudah ada:
    # -> update value
    #
    # Jika key belum ada:
    # -> append ke bucket
    # =========================================
    def insert(self, key, value):

        # Cari index bucket
        index = self.hash_function(key)

        # Ambil bucket pada index tersebut
        bucket = self.table[index]

        # Cek apakah key sudah ada
        for i, (k, v) in enumerate(bucket):

            # Jika key ditemukan
            if k == key:

                # Update value lama
                bucket[i] = (key, value)

                print(f"Data dengan key '{key}' berhasil di-update")
                return

        # Jika key belum ada
        # Tambahkan data baru ke bucket
        bucket.append((key, value))

        print(f"Data '{key}:{value}' berhasil ditambahkan")

    # =========================================
    # Get Function
    # Mengambil value berdasarkan key
    #
    # Return:
    # - value jika ditemukan
    # - None jika tidak ditemukan
    # =========================================
    def get(self, key):

        # Cari index bucket
        index = self.hash_function(key)

        # Ambil bucket
        bucket = self.table[index]

        # Cari key di bucket
        for k, v in bucket:

            if k == key:
                return v

        # Jika tidak ditemukan
        return None

    # =========================================
    # Delete Function
    # Menghapus data berdasarkan key
    #
    # Return:
    # - True jika berhasil
    # - False jika gagal
    # =========================================
    def delete(self, key):

        # Cari index bucket
        index = self.hash_function(key)

        # Ambil bucket
        bucket = self.table[index]

        # Cari posisi data
        for i, (k, v) in enumerate(bucket):

            if k == key:

                # Hapus data
                del bucket[i]

                print(f"Data dengan key '{key}' berhasil dihapus")
                return True

        # Jika key tidak ditemukan
        print(f"Key '{key}' tidak ditemukan")
        return False

    # =========================================
    # Display Function
    # Menampilkan seluruh isi hash table
    # =========================================
    def display(self):

        print("\n===== ISI HASH TABLE =====")

        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")

        print("==========================\n")


# =========================================
# PROGRAM UTAMA
# =========================================

# Membuat object hash table
ht = HashTable()

# Insert data
ht.insert("andi", 20)
ht.insert("budi", 25)
ht.insert("cici", 30)

# Menampilkan isi hash table
ht.display()

# Menambahkan key yang hasil hash-nya sama
ht.insert("dani", 35)

# Tampilkan hash table
ht.display()

# Mengambil data berdasarkan key
print("Umur andi:", ht.get("andi"))
print("Umur budi:", ht.get("budi"))

# Update data
ht.insert("budi", 21)

# Menampilkan isi terbaru
ht.display()

# Menghapus data
ht.delete("budi")

# Menampilkan isi setelah delete
ht.display()

# Mencari data yang tidak ada
print("Umur joko:", ht.get("joko"))