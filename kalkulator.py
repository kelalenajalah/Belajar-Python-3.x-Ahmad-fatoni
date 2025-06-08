print(20*"=", "\nKalkulator dua Variabel\n", 20*"=")

angka_pertama = float(input("Masukan angka pertama : "))
oprator = input("Masukan oprator (+, -, /, *) : ")
angka_kedua = float(input("Masukan angka kedua : "))

if oprator == "+" :
    hasil = angka_pertama + angka_kedua
    print(f"Hasilnya adalah : {hasil}")
elif oprator == "-" :
    hasil = angka_pertama - angka_kedua
    print(f"Hasilnya adalah : {hasil}")
elif oprator == "/" :
    hasil = angka_pertama / angka_kedua
    print(f"Hasilnya adalah : {hasil}")
elif oprator == "*" or oprator == "x" :
    hasil = angka_pertama * angka_kedua
    print(f"Hasilnya adalah : {hasil}")
else :
    print("Angka yang kamu masukan anomali")