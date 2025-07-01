data = ["1","2","3","4","5"]

def isi_data(nominal):
    angka = nominal.copy()
    for nomer in nominal:
        print(f"Ini adalah isi dari data {nomer}")

isi_data(data)

print(30*"=")

def angka_dari_data(nomernya):
    var = nomernya.copy()
    for asal in nomernya:
        print(f"isi dari datanta adalah angka : {asal}")

data2 = ["1","2","3","4","5"]
angka_dari_data(data2)

