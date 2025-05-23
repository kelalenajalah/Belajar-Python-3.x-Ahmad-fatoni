import datetime

mahasiswa1 = {
    'nama':'dudung',
    'nim':'3721837',
    'sks':'123',
    'beasiswa':True,
    'lahir':datetime.datetime(2004,3,12)
}

mahasiswa2 = {
    'nama':'otong',
    'nim':'354537',
    'sks':'118',
    'beasiswa':False,
    'lahir':datetime.datetime(2000,12,2)
}

mahasiswa3 = {
    'nama':'samsul',
    'nim':'40237434',
    'sks':'100',
    'beasiswa':False,
    'lahir':datetime.datetime(1995,2,5)
}

Data_Mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<12} {'SKS':<10}{'BEASIWA':<15} {'LAHIR':<12}") #Untuk nama di atas
print("-"*50)

for mahasisawa in Data_Mahasiswa:
    KEY = mahasisawa

    NAMA = Data_Mahasiswa[KEY]['nama']
    NIM = Data_Mahasiswa[KEY]['nim']
    SKS = Data_Mahasiswa[KEY]['sks']
    BEASISWA = Data_Mahasiswa[KEY]['beasiswa']
    LAHIR = Data_Mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<12} {SKS:<10} {str(BEASISWA):<15} {LAHIR:<12}") # Untuk isi database