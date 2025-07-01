def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",170,40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[2]
    berat = data[2]

    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong",190,54])