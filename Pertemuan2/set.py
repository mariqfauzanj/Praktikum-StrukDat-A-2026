# 1. set
data = {"aku", "kau", "uka"}
print(data)

# induplicate
data = {"a", "b", "c", "a"}
print(data)

data = {"a", "b", "c", True, 1, 2}
print(data)

# type()
data = {"a", "b", "c"}
print(type(data))

# 2. akses set
angka = {"satu", "dua", "tiga"}
for x in angka:
  print(x)

# check present
cek = {"x", "y", "z"}
print("y" in cek)

# 3. add set
# add item
coklat = {"kacang", "almond", "mede"}
coklat.add("hitam")
print(coklat)

# add iterable
coklat = {"kacang", "almond", "mede"}
tambah = ["hitam", "putih"]
coklat.update(tambah)
print(coklat)

# 3. remove set
# remove item
coklat = {"kacang", "almond", "mede"}
coklat.remove("kacang")
print(coklat)

# discard item
coklat = {"kacang", "almond", "mede"}
coklat.discard("kacang")
print(coklat)