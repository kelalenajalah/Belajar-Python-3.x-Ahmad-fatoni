# def tambah(*data):
#     outup = 0
#     for angka in data:
#         outup += angka

#     return outup

# nomer = (1,2,3,4,5)
# print(f"Hasilnya = {tanbah(*nomer)}")

print(20*"=")

def tambah(*data): # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    for angka in data:
        output += angka
    
    return output

hasil = tambah(1,2,3,4,5)
print(f"hasil = {hasil}")

hasil = tambah(10,5,15)
print(f"hasil = {hasil}")

print(20*"=")

print(f"Hasilnya = {tambah(1,2,3,4,5)}")


print(f"Nominalnya 45 = {tambah()}")

