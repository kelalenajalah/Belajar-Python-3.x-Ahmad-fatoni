data = {
   "M" : "Meja",
   "K" : "Kursi",
   "H" : "Heandphone",
   "B" : "Buku",
   "P" : "Pensil"
}

for isi in data:
    print(isi)

Nama_barang = {
    "M" : "Meja",
    "K" : "Kursi",
    "H" : "Heandphone",
    "B" : "Buku",
    "P" : "Pensil"
}

keys = Nama_barang.keys() # Untuk mengabil nama depan saja atau Keys
print(keys)

for keys in Nama_barang.keys(): #key adalah kode yang di gunakan conroh (M)
    print(keys)

value = Nama_barang.values()
print(value)

for value in Nama_barang.values(): #Value adalah nama yang di gunakan conroh (Meja)
    print(value)
    
items = Nama_barang.items()  #Item untuk menampilkan keseluruhan data ("M" : "Meja")
print(f"Nama items: {items}\n")

for items in Nama_barang.items():
    print(f"Key: {keys}, Value: {value}")