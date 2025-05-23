import os
import datetime
import random
import string

Tamplate_barang = {
    'nama': '',
    'Judul buku': '',
    'Nomer seri': '',
    'Tanggal_pinjam': datetime.datetime(1111,1,11)
}

database_barang = {}  # ⬅️ Ini tempat menyimpan data pinjaman

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG DI PERPUSTAKAAN LAFY':^50}")
    print(f"{'SILAHKAN ISI DATA DIRI':^50}")
    print("-"*50)

    barang = dict.fromkeys(Tamplate_barang.keys())
    barang['nama'] = input("Masukan nama : ")
    barang['Judul buku'] = input("Masukan judul buku: ")
    barang['Nomer seri'] = input("Masukan nomer seri: ")
    TAHUN_PINJAM = int(input("Masukan tahun (YYYY): "))
    BULAN_PINJAM = int(input("Masukan bulan (MM): "))
    HARI_PINJAM = int(input("Masukan hari (DD): "))
    barang['Tanggal_pinjam'] = datetime.datetime(TAHUN_PINJAM,BULAN_PINJAM,HARI_PINJAM)

    KEY = ''.join((random.choice(string.ascii_uppercase)
        for i in range(6)))
    database_barang[KEY] = barang  # ⬅️ Simpan data ke database, bukan template

    print("\nDATA PINJAMAN:")
    print(f"{'NO':<8} {'NAMA':<15} {'JUDUL BUKU':<20} {'NOMER SERI':<15} {'TANGGAL PINJAM':<15}")
    print("-"*80)

    for no, (key, data) in enumerate(database_barang.items(), start=1):
        NAMA = data['nama']
        JUDUL_BUKU = data['Judul buku']
        NOMER_SERI = data['Nomer seri']
        TANGGAL_PINJAM = data['Tanggal_pinjam'].strftime("%d-%m-%Y")

        print(f"{no:<8} {NAMA:<15} {JUDUL_BUKU:<20} {NOMER_SERI:<15} {TANGGAL_PINJAM:<15}")

    is_done = input("\nApakah masih pinjam buku (y/n)? ")
    if is_done.lower() == "n":
        break

print("\nTERIMA KASIH SUDAH MEMINJAM BUKU")
