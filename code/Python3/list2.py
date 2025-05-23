# Umtuk memilih satu data angka

data_angka = [i for i in range(1,10)]
print(f"Data angka adalah {data_angka}")

jumplah_data_4 = data_angka.count(4)
jumplah_data_3 = data_angka.count(3)

print(f"Jumplah data angka 4 = {jumplah_data_4}")
print(f"Jumplah data angka 3 = {jumplah_data_3}")

print(10*"=")

# Ambil posisi data dengan index

data = ["Meja", "Pensil", "Penggaris"]

index_Meja = data.index("Meja")
index_pensil = data.index("Pensil")
index_Penggaris = data.index("Penggaris")
print(f"Data index dari Meja = {index_Meja}")
print(f"Data index dari Pensil = {index_pensil}")
print(f"Data index dari Penggaris = {index_Penggaris}")

print(10*"=")

# Menggunakan list menjadi angka urutan

data_angka2 = [1,2,5,4,6,9,3,7,0,]
print(f"Angka acak = {data_angka2}")

data_angka2.sort()
print(f"Data angka Urutkan = {data_angka2}")

data_angka2.reverse()
print(f"Data angka Urutkan di balik = {data_angka2}")
