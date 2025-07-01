data_1 = ["Meja",]
data_2 = ["Kursi"]
data_3 = ["Komputer"]

data_list = [data_1, data_2,data_3]
print(data_list)
print(f"Ini adalah data = {data_list}")

data_0 = ["Meja", "50cm", "Rp.990.500"]
data_1 = ["Kursi", " 40cm", "Rp.450.000"]
data_2 = ["Komputer", "50cm", "Rp.53.000.000"]

Benda = [data_0, data_1, data_2]

for barang in Benda:
    print(f"Jenis \t= {barang[0]}")
    print(f"Ukuran \t= {barang[1]}")
    print(f"harga \t= {barang[2]}\n")

data_0[2] = "Rp.3.400.000"
print(data_0)

data_copy = data_0.copy()
print(data_copy)