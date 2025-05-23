import tkinter as tk
from tkinter import messagebox

class BukuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Daftar Buku")
        self.daftar_buku = []

        self.judul_label = tk.Label(root, text="Judul Buku:")
        self.judul_label.grid(row=0, column=0, padx=10, pady=5)
        self.judul_entry = tk.Entry(root, width=40)
        self.judul_entry.grid(row=0, column=1, padx=10, pady=5)

        self.penulis_label = tk.Label(root, text="Nama Penulis:")
        self.penulis_label.grid(row=1, column=0, padx=10, pady=5)
        self.penulis_entry = tk.Entry(root, width=40)
        self.penulis_entry.grid(row=1, column=1, padx=10, pady=5)

        self.tambah_button = tk.Button(root, text="Tambah Buku", command=self.tambah_buku)
        self.tambah_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.listbox = tk.Listbox(root, width=60)
        self.listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def tambah_buku(self):
        judul = self.judul_entry.get()
        penulis = self.penulis_entry.get()

        if judul and penulis:
            buku_baru = [judul, penulis]
            self.daftar_buku.append(buku_baru)
            self.perbarui_listbox()
            self.judul_entry.delete(0, tk.END)
            self.penulis_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Salah", "Harap isi judul dan penulis!")

    def perbarui_listbox(self):
        self.listbox.delete(0, tk.END)
        for index, buku in enumerate(self.daftar_buku):
            self.listbox.insert(tk.END, f"{index+1}. Judul: {buku[0]} | Penulis: {buku[1]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BukuApp(root)
    root.mainloop()
