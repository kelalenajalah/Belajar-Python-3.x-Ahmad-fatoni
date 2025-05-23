import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
import string
import random

# Template data mahasiswa
mahasiswa_template = {
    'nama': '',
    'nim': '',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 1)
}

data_mahasiswa = {}

# Fungsi untuk menambahkan data
def tambah_data():
    try:
        nama = entry_nama.get()
        nim = entry_nim.get()
        sks = int(entry_sks.get())
        tahun = int(entry_tahun.get())
        bulan = int(entry_bulan.get())
        tanggal = int(entry_tanggal.get())
        lahir = datetime.datetime(tahun, bulan, tanggal)

        mahasiswa = dict.fromkeys(mahasiswa_template.keys())
        mahasiswa['nama'] = nama
        mahasiswa['nim'] = nim
        mahasiswa['sks_lulus'] = sks
        mahasiswa['lahir'] = lahir

        key = ''.join(random.choices(string.ascii_uppercase, k=6))
        data_mahasiswa[key] = mahasiswa

        tampilkan_data()
        clear_form()
    except Exception as e:
        messagebox.showerror("Input Error", f"Data tidak valid:\n{e}")

# Fungsi untuk menampilkan data di Treeview
def tampilkan_data():
    for i in tree.get_children():
        tree.delete(i)
    for key, mhs in data_mahasiswa.items():
        tree.insert('', 'end', values=(
            key,
            mhs['nama'],
            mhs['nim'],
            mhs['sks_lulus'],
            mhs['lahir'].strftime("%d-%m-%Y")
        ))

# Fungsi untuk mengosongkan form
def clear_form():
    entry_nama.delete(0, tk.END)
    entry_nim.delete(0, tk.END)
    entry_sks.delete(0, tk.END)
    entry_tahun.delete(0, tk.END)
    entry_bulan.delete(0, tk.END)
    entry_tanggal.delete(0, tk.END)

# Buat window utama
root = tk.Tk()
root.title("Aplikasi Data Mahasiswa")
root.geometry("700x500")
root.config(bg="#f0f4f7")

# Judul
judul = tk.Label(root, text="Data Mahasiswa", font=("Helvetica", 18, "bold"), bg="#f0f4f7")
judul.pack(pady=10)

# Frame input
frame_input = tk.Frame(root, bg="#f0f4f7")
frame_input.pack(pady=10)

# Nama
tk.Label(frame_input, text="Nama", bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

# NIM
tk.Label(frame_input, text="NIM", bg="#f0f4f7").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_nim = tk.Entry(frame_input)
entry_nim.grid(row=1, column=1, padx=5, pady=5)

# SKS
tk.Label(frame_input, text="SKS Lulus", bg="#f0f4f7").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_sks = tk.Entry(frame_input)
entry_sks.grid(row=2, column=1, padx=5, pady=5)

# Tanggal Lahir
tk.Label(frame_input, text="Tahun Lahir", bg="#f0f4f7").grid(row=0, column=2, padx=5, pady=5)
entry_tahun = tk.Entry(frame_input, width=8)
entry_tahun.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_input, text="Bulan", bg="#f0f4f7").grid(row=1, column=2, padx=5, pady=5)
entry_bulan = tk.Entry(frame_input, width=5)
entry_bulan.grid(row=1, column=3, padx=5, pady=5)

tk.Label(frame_input, text="Tanggal", bg="#f0f4f7").grid(row=2, column=2, padx=5, pady=5)
entry_tanggal = tk.Entry(frame_input, width=5)
entry_tanggal.grid(row=2, column=3, padx=5, pady=5)

# Tombol
frame_btn = tk.Frame(root, bg="#f0f4f7")
frame_btn.pack(pady=10)
btn_tambah = tk.Button(frame_btn, text="Tambah Data", command=tambah_data, bg="#4caf50", fg="white", padx=10)
btn_tambah.pack(side="left", padx=5)
btn_keluar = tk.Button(frame_btn, text="Keluar", command=root.destroy, bg="#f44336", fg="white", padx=10)
btn_keluar.pack(side="left", padx=5)

# Tabel
tree = ttk.Treeview(root, columns=('KEY', 'Nama', 'NIM', 'SKS', 'Lahir'), show='headings')
tree.heading('KEY', text='KEY')
tree.heading('Nama', text='Nama')
tree.heading('NIM', text='NIM')
tree.heading('SKS', text='SKS Lulus')
tree.heading('Lahir', text='Tanggal Lahir')
tree.pack(pady=20, fill=tk.X)

root.mainloop()
