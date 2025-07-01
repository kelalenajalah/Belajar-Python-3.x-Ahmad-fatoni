import program.matematika as matematika
import sains as angka 

gaya = angka(2,3)
print(f"Nominal {gaya}")


import modul.program
from program import fisika
from program import gaya as force

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")

gaya = force(90,10)
print(f"gaya adalah = {gaya}")