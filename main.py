print("\nPROGRAM PEMBBUAT TEMPEREATURE\n")
      
#Untuk mencari Celcius
celcius = float(input('Masukan suhu dalam celcius : '))
print("Suhu adalah : ", celcius, "celcius")
print("Suhu dalam reamur : ", celcius * (4/5), "reamur" )
print("Suhu dalam farenheit adalah : ", (celcius * 9/5) + 32, "farenheit")
print("Suhu dalam kelvin adalah : ", celcius + 273, "kelvin")

print("\n======================================\n")

#Untuk mencari Fahrenheit
farenheit = float(input("Masukan suhu dalam Farenheit : "))
print("suhu dalam farenheit : ", farenheit, "farenheit")
print("suhu dalam kelvin : ", (farenheit - 32) * 5/9 + 273, "farenheit")
print("Suhu dalam reamur : ", (4/9 * (farenheit - 32)), "Reamur")
print("Suhu dalam celcius : ", (farenheit - 32) * 5/9, "Celcius")

print("\n======================================\n")

#Untuk mencari reamur
reamur = float(input ("Masukan Suhu dalam Reamur : "))
print("suhu dalalm reamue : ", reamur, "reamur")
print("suhu dalam kelvin : ", (reamur * 5/4) + 273, "kelvin")
print("Suhu dalam farenheit : ", (reamur * 9/4) + 32, "Fahrenheit")
print("Suhu dalam celcius : ", reamur / 0.8, "Celcius")

print("\n======================================\n")

#Untuk mencari reamur
kelvin = float(input ("masukan Suhu dalam kelvin : "))
print("suhu dalam kelvin : ", kelvin, 'kelvin')
print("suhu dalam celcius", kelvin - 273 , "Celcius")
print("Suhu dalam farenheit : ", (kelvin - 273.15) * 9/5 + 32, "Fahrenheit")
print("Suhu dalam reamur : ", (4/5) * (kelvin - 273.15), "reamur")
