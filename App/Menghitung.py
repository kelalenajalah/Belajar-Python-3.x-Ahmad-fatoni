import os

# os.system("clear")
# print(f"{'MENGHITUNG LUAS DAN KELILING':^40}")
# print(f"{'DARI PERSEGI PANJANG':^40}")
# print(40*"=")

# # Mengambil input dari user yang di masukan
# PANJANG = int(input("Masukan Lebar : "))
# LEBAR = int(input("Masukan Panjang : "))

# # Program rumus
# LUAS = PANJANG*LEBAR
# KELILING = 2(PANJANG*LEBAR)

# # Untuk menampilkan hasilnya 
# print(f"Luas dari persegi LUAS adalah : {LUAS}")
# print(f"Luas dari persegi panjang adalah : {KELILING}")

def header():
    os.system("cls")
    print(f"{'MENGHITUNG LUAS DAN KELILING':^40}")
    print(f"{'DARI PERSEGI PANJANG':^40}")
    print(40*"=")


def dari_user():
    PANJANG = int(input("Masukan Lebar : "))
    LEBAR = int(input("Masukan Panjang : "))
    return PANJANG, LEBAR

def rumus_luas(PANJANG, LEBAR):
    return PANJANG*LEBAR

def rumus_keliling(PANJANG, LEBAR):
    return 2*(PANJANG*LEBAR)

def display(pesannya, value):
    print(f"Hasil adalah: {value}")

# Program yang di jalankan
while True:
    header()
    LEBAR,PANJANG = dari_user()
    LUAS = rumus_luas(PANJANG, LEBAR)
    KELILING = rumus_keliling(PANJANG, LEBAR)

    display("Luas", LUAS)
    display("keliling", KELILING)

    iscontinue = input(f"Apakah masih di lanjutkan (y/n)?")
    if iscontinue == "n":
        break

print("Ini adalah ahkir dari program")