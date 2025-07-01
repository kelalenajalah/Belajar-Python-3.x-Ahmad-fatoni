import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import random
import string

# template dict mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mahasiswa = {}

def generate_key():
    """Menghasilkan kunci acak untuk setiap mahasiswa."""
    return ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

def add_mahasiswa():
    """Menambahkan data mahasiswa ke dictionary dan memperbarui Treeview."""
    nama = entry_nama.get()
    nim = entry_nim.get()
    sks_lulus = entry_sks.get()
    tahun_lahir = entry_tahun.get()
    bulan_lahir = entry_bulan.get()
    tanggal_lahir = entry_tanggal.get()

    if not all([nama, nim, sks_lulus, tahun_lahir, bulan_lahir, tanggal_lahir]):
        messagebox.showwarning("Input Kurang", "Mohon lengkapi semua data mahasiswa.")
        return

    try:
        sks_lulus = int(sks_lulus)
        tahun_lahir = int(tahun_lahir)
        bulan_lahir = int(bulan_lahir)
        tanggal_lahir = int(tanggal_lahir)
        lahir_dt = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)
    except ValueError:
        messagebox.showerror("Input Salah", "Pastikan SKS Lulus dan Tanggal Lahir diisi dengan angka yang benar.")
        return

    mahasiswa = {
        'nama': nama,
        'nim': nim,
        'sks_lulus': sks_lulus,
        'lahir': lahir_dt
    }

    key = generate_key()
    data_mahasiswa.update({key: mahasiswa})
    update_mahasiswa_list()
    clear_entries()
    messagebox.showinfo("Berhasil", "Data mahasiswa berhasil ditambahkan!")

def update_mahasiswa_list():
    """Memperbarui tampilan Treeview dengan data terbaru."""
    for i in tree.get_children():
        tree.delete(i)

    for key, mhs in data_mahasiswa.items():
        tree.insert("", "end", values=(key, mhs['nama'], mhs['nim'], mhs['sks_lulus'], mhs['lahir'].strftime("%x")))

def clear_entries():
    """Mengosongkan semua input field."""
    entry_nama.delete(0, tk.END)
    entry_nim.delete(0, tk.END)
    entry_sks.delete(0, tk.END)
    entry_tahun.delete(0, tk.END)
    entry_bulan.delete(0, tk.END)
    entry_tanggal.delete(0, tk.END)

def delete_mahasiswa():
    """Menghapus data mahasiswa yang dipilih."""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Tidak Ada Pilihan", "Mohon pilih data mahasiswa yang ingin dihapus.")
        return

    confirm = messagebox.askyesno("Konfirmasi Hapus", "Anda yakin ingin menghapus data ini?")
    if confirm:
        for item in selected_item:
            key_to_delete = tree.item(item, "values")[0]
            del data_mahasiswa[key_to_delete]
        update_mahasiswa_list()
        messagebox.showinfo("Berhasil", "Data mahasiswa berhasil dihapus.")

# --- Setup GUI ---
root = tk.Tk()
root.title("Aplikasi Data Mahasiswa")
root.geometry("800x600")
root.resizable(False, False)

# # Mengatur tema
# root.tk.call("source", "azure.tcl") # Pastikan azure.tcl ada di direktori yang sama atau path-nya benar
# root.tk.call("set_theme", "dark")

# Frame Input Data
input_frame = ttk.LabelFrame(root, text="Input Data Mahasiswa", padding=(20, 20))
input_frame.pack(padx=20, pady=20, fill="x")

ttk.Label(input_frame, text="Nama Mahasiswa:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
entry_nama = ttk.Entry(input_frame, width=40)
entry_nama.grid(row=0, column=1, sticky="ew", pady=5, padx=5)

ttk.Label(input_frame, text="NIM Mahasiswa:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
entry_nim = ttk.Entry(input_frame, width=40)
entry_nim.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

ttk.Label(input_frame, text="SKS Lulus:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
entry_sks = ttk.Entry(input_frame, width=40)
entry_sks.grid(row=2, column=1, sticky="ew", pady=5, padx=5)

ttk.Label(input_frame, text="Tanggal Lahir (YYYY-MM-DD):").grid(row=3, column=0, sticky="w", pady=5, padx=5)
date_frame = ttk.Frame(input_frame)
date_frame.grid(row=3, column=1, sticky="ew", pady=5, padx=5)

entry_tahun = ttk.Entry(date_frame, width=8)
entry_tahun.grid(row=0, column=0, padx=2)
ttk.Label(date_frame, text="-").grid(row=0, column=1)
entry_bulan = ttk.Entry(date_frame, width=5)
entry_bulan.grid(row=0, column=2, padx=2)
ttk.Label(date_frame, text="-").grid(row=0, column=3)
entry_tanggal = ttk.Entry(date_frame, width=5)
entry_tanggal.grid(row=0, column=4, padx=2)

# Tombol Aksi
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Tambah Mahasiswa", command=add_mahasiswa, style="Accent.TButton")
add_button.pack(side="left", padx=10)

delete_button = ttk.Button(button_frame, text="Hapus Mahasiswa", command=delete_mahasiswa, style="Accent.TButton")
delete_button.pack(side="left", padx=10)

clear_button = ttk.Button(button_frame, text="Bersihkan Input", command=clear_entries)
clear_button.pack(side="left", padx=10)

# Tampilan Data Mahasiswa (Treeview)
tree_frame = ttk.Frame(root)
tree_frame.pack(padx=20, pady=10, fill="both", expand=True)

columns = ("key", "nama", "nim", "sks_lulus", "tanggal_lahir")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")

tree.heading("key", text="KEY", anchor="w")
tree.heading("nama", text="Nama", anchor="w")
tree.heading("nim", text="NIM", anchor="w")
tree.heading("sks_lulus", text="SKS Lulus", anchor="center")
tree.heading("tanggal_lahir", text="Tanggal Lahir", anchor="center")

tree.column("key", width=80, stretch=tk.NO)
tree.column("nama", width=150, stretch=tk.YES)
tree.column("nim", width=100, stretch=tk.NO)
tree.column("sks_lulus", width=100, stretch=tk.NO)
tree.column("tanggal_lahir", width=120, stretch=tk.NO)

# Scrollbar untuk Treeview
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# Memulai aplikasi
update_mahasiswa_list() # Muat data awal jika ada
root.mainloop()