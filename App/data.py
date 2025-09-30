import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

# Data produk
data = {
    "No": list(range(1, 17)),
    "Nama Produk": [
        "Nasi uduk", "Mie rebus", "Nasi goreng", "Mie goreng",
        "Risol", "Bakwan", "Tahu isi", "Tahu brontak",
        "Tempe goreng", "Mendoan", "Pop ice", "Marimas",
        "Kopi hitam", "Energen", "Susu", "Kopi susu"
    ],
    "Harga": [
        3000, 4000, 5000, 4000,
        2000, 1000, 1000, 1000,
        1000, 1000, 3000, 1500,
        3000, 3000, 3000, 3500
    ]
}

# Buat DataFrame
df = pd.DataFrame(data)

# Tampilkan tabel di terminal
print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))

# Visualisasi grafik batang
plt.figure(figsize=(10, 6))
plt.bar(df["Nama Produk"], df["Harga"])
plt.xticks(rotation=75, ha="right")
plt.ylabel("Harga (Rp)")
plt.title("Perbandingan Harga Produk")
plt.tight_layout()
plt.show()

# Visualisasi pie chart persentase harga
plt.figure(figsize=(8, 8))
plt.pie(df["Harga"], labels=df["Nama Produk"], autopct="%1.1f%%")
plt.title("Persentase Harga Produk")
plt.show()
