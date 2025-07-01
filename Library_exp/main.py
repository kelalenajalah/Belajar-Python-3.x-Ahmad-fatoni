# import io

# file = io.open("teks,txt", "r")
# print(open.read())


import datetime

nama_waktu = datetime.datetime.now()
print(f"Waktu sekarang = {nama_waktu}")
print(f"Tahun sekarang = {nama_waktu.year}")
print(f"Bulan sekarang = {nama_waktu.month}")
print(f"hari sekarang = {nama_waktu.day}")
print(f"hari sekarang = {nama_waktu.strftime('%A')}") # A = Nama hari, a = Nomer hari

