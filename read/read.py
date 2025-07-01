print(3*"=", " Membaca file txt ", 3*"=")
file = open("data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## baca seluruh file
print(file.read())
print(file.readlines())

print(f"Membaca file : {file.readable()}")
print(f"Menulis file file : {file.writable()}")

# print(file.read())

# # Membuka file secara penuh
# print(file.readlines())


print(file.readline(),end="") # baca baris pertama
print(file.readline(),end="") # baca baris kedua

# print((file.readline()), end="")

with open ("data.txt", mode="r",) as file:
    isi = file.readline()
    print(isi, end="")
    print(f"File sudah di baca {file.closed}")

# print(f"File sudah di baca {file.closed}")

