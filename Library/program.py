import tkinter as tk
from tkinter import ttk # Untuk menapilkan windows
from tkinter.messagebox import showinfo # untuk menampilkan POPUP notifikasi

# __init__
window = tk.Tk()
window.configure(bg="white") #Untuk Warna
window.geometry("400x400")
# window.resizable(False,False) #Tidak bisa resize (OPSIONAL)
window.title("Progam sederhana Menyapa !")

# membuat variabel dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Membuat tombol
def tombol():
    Pesanya = (f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} Selamat datang")
    showinfo(title="Apa kabar ?", message=Pesanya)

# Untuk input
input_fream = ttk.Frame(window)

# penempatan Grid, Pack, dan Pleace
input_fream.pack(padx=10, fill="x", expand=True )

# komponennya label nama depan
nama_depan_labelnya = ttk.Label(input_fream, text="Nama depan :")
nama_depan_labelnya.pack(padx=10, fill="x", expand=True )

# Komponen entry nama depan
entry_nama_depan = ttk.Entry(input_fream, textvariable=NAMA_DEPAN)
entry_nama_depan.pack(padx=10, fill="x", expand=True )

# komponennya nama belakang
nama_belakang_labelnya = ttk.Label(input_fream, text="Nama belakang :")
nama_belakang_labelnya.pack(padx=10, fill="x", expand=True )

# Komponen entry nama belakang
entry_nama_belakang = ttk.Entry(input_fream, textvariable=NAMA_BELAKANG)
entry_nama_belakang.pack(padx=10, fill="x", expand=True )

# Komponen tombol
tombol = ttk.Button(input_fream, text="Menyapa !", command= tombol)
tombol.pack(fill="x", expand=True, padx=10, pady=10 )

window.mainloop() #Untuk mengulangi dan tidak berhenti di window