print("Ahkir dari program")

sisi = 4

print("Awal for")
count = 1
for i in range(sisi):
    count += 1
    print("*"*count)

print("Ahkir dari program")

print(15*"=", "Menggunakan while", 15*"=")# Mengguunkaan while

print("Awal dari program")

sisi = 10

count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi:
        break

print("Ahkir dari program")

print(15*"=", "Menggunakan while", 15*"=")

print("Awal dari program")

sisi = 10

count = 1
while True:
    if (count%2):
        print("*"*count)
        count += 1

    else:
        count += 1
        continue

    if count > sisi:
        break

print("Ahkir dari program")