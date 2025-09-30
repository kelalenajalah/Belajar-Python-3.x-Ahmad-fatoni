print("CALCULATOR")

angkaPertama = input(float("Masukan angka :"))
angkaKedua = input(float("Masukan angka :"))
oprasi = input("Masukan oprasi (+,-,/,x)")

if oprasi == "+":
    hasil = angkaPertama + angkaKedua
    print(f"Hasil dari {angkaPertama} + {angkaKedua} = {hasil}")
elif oprasi == "-":
    hasil = angkaPertama - angkaKedua
    print(f"Hasil dari {angkaPertama} - {angkaKedua} = {hasil}")
elif oprasi == "*" or oprasi == "x":
    hasil = angkaPertama * angkaKedua
    print(f"Hasil dari {angkaPertama} x {angkaKedua} = {hasil}")
elif oprasi == "/":
    hasil = angkaPertama / angkaKedua
    print(f"Hasil dari {angkaPertama} / {angkaKedua} = {hasil}")
elif lanjutkan == "7" 