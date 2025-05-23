# Contoh penggunaan pass (Tidak akan di gunakan)
print(10*"=","Pass",10*"=")

angka = 0 

while angka < 5:
    angka += 1
    if angka == 3:
        pass #tidak akan di gunakan
    print(angka)

print(10*"=","continue",10*"=")

# Untuk penggunaan Continue

angka = 0

while angka < 5:
    angka += 1
    print(f"Angka sekarang adalah -> {angka}")

    if angka == 3:
        print("Skip") # Akan di tambah kemungkinan di dalam alur(Melanjutkan saja/di Skip)
        continue
    print("Lanjutkan")

print("Aksi dari alur telah selesai")

# Untuk penggunaan break (Menggunakan angka sendiri)

print(10*"=","Break",10*"=")

angka = 0
while True:
    angka += 1
    print(f"Angka sekarang adalah -> {angka}")

    if angka == 9:
        print("Berhenti saat sudah pas") # akan berhenti jika sudah ketemu
        break
    print("Stoppp!!!")

print("Aksi dari alur telah selesai")

# Untuk penggunaan break (Menggunakan angka program)

print(10*"=","Break otomatis",10*"=")

angka = 0

data_int = int(input("Masukan jumplahnya = "))
while True:
    angka += 1
    print(f"Angka sekarang adalah -> {angka}")

    if angka == data_int:
        print("Berhenti saat sudah pas") # akan berhenti jika sudah ketemu dengan data yang di mauskan sendiri
        break
    print("Stoppp!!!")

print("Aksi dari alur telah selesai")


print(10*"=","Break dengan data yang di codingnya",10*"=")