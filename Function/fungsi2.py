def oprasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    bagi = angka1 / angka2
    kali = angka1 * angka2

    return tambah, kurang, bagi, kali

# print(oprasi_matematika(5,5))

k,l,m,n = oprasi_matematika(5,5)

print(f"Ini hasil dari tambah = {k}")
print(f"Ini hasil dari kurang = {l}")
print(f"Ini hasil dari bagi = {m}")
print(f"Ini hasil dari kali = {n}")

def hello(nama): # type: ignore
    print(f"Selmat datang {nama}")

hello("abdul")

def 