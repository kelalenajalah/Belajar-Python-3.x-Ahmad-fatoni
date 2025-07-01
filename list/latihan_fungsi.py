import os

def header():
    """Header Aplikasi"""
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    """User Input"""
    lebar = int(input("Masukkan lebar : "))
    panjang = int(input("Masukkan panjang : "))
    return lebar, panjang

def hitung_luas(lebar, panjang):
    """fungsi luas"""
    return lebar*panjang

def hitung_keliling(lebar, panjang):
    """fungsi keliling"""
    return 2*(lebar+panjang)

def display(message, value):
    """fungsi display"""
    print(f"Hasil perhitungan {message} adalah {value}")

while True:
    header()

    operasi = int(input("1. Hitung luas dan keliling\n2. Hitung luas saja \n3. Hitung keliling saja\nMasukkan operasi yang anda inginkan (1/2/3) : "))

    if operasi == 1:
        LEBAR, PANJANG = input_user()
        LUAS = hitung_luas(LEBAR, PANJANG)
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("luas", LUAS)
        display("keliling", KELILING)
    elif operasi == 2:
        LEBAR, PANJANG = input_user()
        LUAS = hitung_luas(LEBAR, PANJANG)
        display("luas", LUAS)
    elif operasi == 3:
        LEBAR, PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("keliling", KELILING)
    else:
        print("Masukan operator 1 / 2 / 3")

    isContinue = input("Apakah ingin lanjut y/n : ")
    if isContinue == "n":
        break

print("Terima Kasih!")