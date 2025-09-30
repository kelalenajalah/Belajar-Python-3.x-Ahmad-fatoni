# ef hello_world(nama: str): 
#     '''Untuk memanggil nama seseorang'''
#     print(f"Selamat datang wahai {nama}")

# hello_world("toni")

# def angka(angka_1:int, angka_2:int):
#     hasil = angka_1 + angka_2
#     print(f"{angka_1}+{angka_2}={hasil}")

# angka(1,2)

# isiannya("Nama hewan")

# print(20*"=")

# def positional_arguments (a,b):
# 	print(f"Ini inputan {b}")
# 	print (f"Sedangkan ini inputan {a}")

# positional_arguments("a", "b")

# print(20*"=")

def matematika(angka1, angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

matematika(3,32)

# print(20*"=")

daftar_alat = ["barble", "duble", "gym", "mboh", "apa bar"]

def alat_gym(aja):
    nama_alat = aja.copy()
    for kegunaan in nama_alat:
        print(f"Nama alat adalah {kegunaan}")

alat_gym(daftar_alat)