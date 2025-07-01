import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Setup window
window = tk.Tk()
window.configure(bg="white")
window.geometry("400x400")
window.title("Kalkulator Sederhana")

# Variabel input
ANGKA_PERTAMA = tk.StringVar()
OPRATOR = tk.StringVar()
ANGKA_KEDUA = tk.StringVar()

# Fungsi Kalkulasi
def kalkulator():
    try:
        angka1 = float(ANGKA_PERTAMA.get())
        angka2 = float(ANGKA_KEDUA.get())
        operator = OPRATOR.get().strip()

        if operator == "+":
            hasil = angka1 + angka2
        elif operator == "-":
            hasil = angka1 - angka2
        elif operator == "*" or operator.lower() == "x":
            hasil = angka1 * angka2
        elif operator == "/":
            hasil = angka1 / angka2
        else:
            showinfo("Error", "Operator tidak valid! Gunakan +, -, *, atau /")
            return

        pesan = f"Hasil dari {angka1} {operator} {angka2} = {hasil}"
        showinfo("Hasil Kalkulasi", pesan)

    except ValueError:
        showinfo("Error", "Masukkan angka yang valid!")
    except ZeroDivisionError:
        showinfo("Error", "Tidak bisa dibagi dengan nol!")

# GUI Layout
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Angka pertama
ttk.Label(input_frame, text="Masukkan angka pertama:").pack(fill="x")
ttk.Entry(input_frame, textvariable=ANGKA_PERTAMA).pack(fill="x")

# Operator
ttk.Label(input_frame, text="Masukkan operator (+, -, *, /):").pack(fill="x")
ttk.Entry(input_frame, textvariable=OPRATOR).pack(fill="x")

# Angka kedua
ttk.Label(input_frame, text="Masukkan angka kedua:").pack(fill="x")
ttk.Entry(input_frame, textvariable=ANGKA_KEDUA).pack(fill="x")

# Tombol hasil
ttk.Button(input_frame, text="Hitung", command=kalkulator).pack(pady=20)

# Jalankan aplikasi
window.mainloop()
