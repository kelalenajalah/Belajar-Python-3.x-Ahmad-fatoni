import os
os.system("cls")
print(f"{'INI ADALAH KALKULATOR SEDERHANA':^50}")

angka1 = float(input("Masukan angka pertama :"))
oprator = input("Masukan opratornya (+,-,x,/):")
angka2= float(input("Masukan angka kedua :"))

if oprator == "+" :
    hasil = angka1 + angka2
    print(f"Hasilnya adalah {hasil}")
if oprator == "-" :
    hasil = angka1 - angka2
    print(f"Hasilnya adalah {hasil}")
if oprator == "*" or oprator == "x" :
    hasil = angka1 * angka2
    print(f"Hasilnya adalah {hasil}")
if oprator == "/" :
    hasil = angka1 / angka2
    print(f"Hasilnya adalah {hasil}")
else:
    print("Angka yang kamu masukan salah")