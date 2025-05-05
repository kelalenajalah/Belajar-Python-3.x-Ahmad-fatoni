import tkinter as tk
from tkinter import messagebox

def konversi_suhu():
    try:
        suhu = float(entry.get())
        satuan = var.get()

        if satuan == "Celcius":
            reamur = suhu * 4/5
            fahrenheit = (suhu * 9/5) + 32
            kelvin = suhu + 273
        elif satuan == "Fahrenheit":
            reamur = 4/9 * (suhu - 32)
            kelvin = (suhu - 32) * 5/9 + 273
            fahrenheit = suhu
            suhu = (suhu - 32) * 5/9  # Celcius
        elif satuan == "Reamur":
            kelvin = (suhu * 5/4) + 273
            fahrenheit = (suhu * 9/4) + 32
            suhu = suhu / 0.8  # Celcius
            reamur = suhu * 4/5
        elif satuan == "Kelvin":
            suhu = suhu - 273
            reamur = suhu * 4/5
            fahrenheit = (suhu * 9/5) + 32
            kelvin = suhu + 273
        else:
            raise ValueError("Satuan tidak dikenali")

        result = f"""Hasil Konversi:
Celcius: {suhu:.2f}
Reamur: {reamur:.2f}
Fahrenheit: {fahrenheit:.2f}
Kelvin: {kelvin:.2f}"""
        messagebox.showinfo("Hasil Konversi", result)

    except ValueError:
        messagebox.showerror("Input Salah", "Masukkan angka suhu yang valid!")

root = tk.Tk()
root.title("Konversi Suhu")

tk.Label(root, text="Masukkan Suhu:").pack()
entry = tk.Entry(root)
entry.pack()

var = tk.StringVar(value="Celcius")
tk.OptionMenu(root, var, "Celcius", "Fahrenheit", "Reamur", "Kelvin").pack()

tk.Button(root, text="Konversi", command=konversi_suhu).pack()

root.mainloop()
