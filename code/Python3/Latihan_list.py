Daftar_buku = []
while True:
    print("Daftar buku baru")
    Judul = input("Masukan Judul :")
    Penulis = input("Masukan Penulis :")

    Buku_baru = [Judul, Penulis]
    Daftar_buku.append(Buku_baru)

    print("\n","="*10,"Data Buku","="*10)
    for index, buku in enumerate(Daftar_buku):
        print(f"\t{index+1} | {buku[+1]} | {buku[+1]}")

    print("="*32,"\n")
    isdilanjutkan = input("Apakah mau di lanjutkan ?(y/n)")

    if isdilanjutkan == "n":
        break

print("PROGRAM SELESAI")
