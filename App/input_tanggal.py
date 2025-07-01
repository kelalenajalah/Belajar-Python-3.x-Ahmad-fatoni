import datetime as dt

print("Masukan tangal, \nBulan dan Tahun lahir akamu\n")
tanggal = int(input("Tanggal \t:"))
Bulan = int(input("Bulan \t\t:"))
Tahun = int(input("Tanggal \t:"))

tanggal_lahir = dt.date(Tahun,Bulan,tanggal)
print(f"Tanggal lahir kamu adalah : {tanggal_lahir}")

#Untuk tanggal hari ini menggunakan 
hari_ini = dt.date.today()
print(f"tanggal hari ini adalah : {hari_ini}")
hari_ini = hari_ini - tanggal_lahir
umur_tahun = hari_ini.days // 365
umur_bulan_sisa =  (hari_ini.days % 365) // 30

#Output
print(f"Hari saya adalah :{tanggal_lahir:%A}") #Untuk menampilkan hari
print(f"Umur kamu adalah : {umur_tahun} Tahun, {umur_bulan_sisa} Bulan")


#Rumus dari Modulus dan Devusion

# Operasi	Hasil	Penjelasan
# a / b 	4.25	Pembagian biasa (float)
# a // b	4	    Pembagian bulat
# a % b	    1	    Sisa dari pembagian