import matplotlib.pyplot as plt

nama = ["Andi", "Budi", "Cici", "Dodi", "Eka"]
nilai = [80, 75, 90, 60, 85]

plt.bar(nama, nilai)
plt.title("Nilai Ujian Siswa")
plt.xlabel("Nama Siswa")
plt.ylabel("Nilai")
plt.show()
