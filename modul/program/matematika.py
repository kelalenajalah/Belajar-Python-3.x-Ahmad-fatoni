# ini program matematika tambah dengan args

def tambah(*data):
    output = 0
    for angka in data:
        output += angka

    return output

hasilnya = tambah(1,2,3,4,5)
print(f"Ini hasilnya = {hasilnya}")

# ini program matematika kali dengan args

def kali(*data):
    output = 1
    for angka in data:
        output *= angka

    return output

hasilnya = kali(1,2,3,4,5)
print(f"Ini hasilnya = {hasilnya}")

# Untuk program pangkat

def pangkat(n):
    return lambda angka:angka**n

hasilnya = pangkat(2)
print(f"Hasilnya adalah = {hasilnya}")
