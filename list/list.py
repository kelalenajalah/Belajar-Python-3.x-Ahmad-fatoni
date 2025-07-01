# Untuk penggunaan list biasa

data_angka = [1,2,3,4,5]
print(data_angka)

data_nama = ["saya", "adalah", "siapa"] # String waajib menggunakan "..."
print(data_nama)

data_boolean = [True, False, True, True]
print(data_boolean)

data_campuran = [1, "Masako", True, 2, "micin", False]
print(data_campuran)

# Alternatif membuat list
data_range = range(0,10,5)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop 
list_dengan_for = [i for i in range(1, 12)] # Menampikan angka sesua dalam (...)
print(list_dengan_for) 

# Membuat list pake for pake if

list_dengan_for_if = [i for i in range(0, 10) if i != 5 ] # Maka 5 akan tidak sama dengan
print(list_dengan_for_if) # Anngka 5 tidak akan di tampilkan

Mencari_bilangan_genap = [i for i in range(0, 10) if i%2 == 0 ] # %2 dan == Untuk mencari bilangan genap
print(Mencari_bilangan_genap) # Bilangan genap rentan 0 sampai dengan 10 (Untuk mecari bilangan klipatan 2)

Mencari_bilangan_ganjil = [i for i in range(0, 10) if i%2 != 0 ] # %2 dan != Untuk mencari bilangan Ganjil
print(Mencari_bilangan_ganjil) # Bilangan ganjil rentan 0 sampai dengan 10 (Untuk mencari bilangan tidak sama dengan 2)


