import tkinter as tk

def klik(tombol):
    if tombol == "=":
        try:
            hasil = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(hasil))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif tombol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, tombol)

root = tk.Tk()
root.title("Kalkulator Sederhana")

entry = tk.Entry(root, width=24, font=("poppins", 18))
entry.grid(row=0, column=0, columnspan=4)

tombol_list = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row, col = 1, 0
for tombol in tombol_list:
    tk.Button(root, text=tombol, width=5, height=2,
              command=lambda t=tombol: klik(t)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="C", width=22, height=2, command=lambda: klik("C")).grid(row=row, column=0, columnspan=4)

root.mainloop()
