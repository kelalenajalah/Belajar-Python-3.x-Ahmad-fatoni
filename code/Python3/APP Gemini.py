import tkinter as tk
from tkinter import messagebox, scrolledtext

class AplikasiBuku:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Buku Sederhana")
        self.root.geometry("600x600") # Ukuran jendela awal
        self.root.resizable(False, False) # Nonaktifkan resize jendela

        self.daftar_buku = []

        # Frame untuk input buku
        self.frame_input = tk.LabelFrame(root, text="Tambah / Cari Buku", padx=10, pady=10)
        self.frame_input.pack(pady=10, fill="x", padx=10)

        tk.Label(self.frame_input, text="Judul:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_judul = tk.Entry(self.frame_input, width=40)
        self.entry_judul.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_input, text="Penulis:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_penulis = tk.Entry(self.frame_input, width=40)
        self.entry_penulis.grid(row=1, column=1, padx=5, pady=5)

        # Tombol Aksi
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=5)

        self.btn_tambah = tk.Button(self.frame_buttons, text="Tambah Buku", command=self.tambah_buku, width=15)
        self.btn_tambah.grid(row=0, column=0, padx=5, pady=5)

        self.btn_tampilkan = tk.Button(self.frame_buttons, text="Tampilkan Semua", command=self.tampilkan_semua_buku, width=15)
        self.btn_tampilkan.grid(row=0, column=1, padx=5, pady=5)

        self.btn_cari = tk.Button(self.frame_buttons, text="Cari Buku", command=self.cari_buku, width=15)
        self.btn_cari.grid(row=0, column=2, padx=5, pady=5)

        self.btn_hapus = tk.Button(self.frame_buttons, text="Hapus Buku", command=self.hapus_buku, width=15)
        self.btn_hapus.grid(row=0, column=3, padx=5, pady=5)
        
        # Frame untuk menampilkan daftar buku
        self.frame_list = tk.LabelFrame(root, text="Daftar Buku", padx=10, pady=10)
        self.frame_list.pack(pady=10, fill="both", expand=True, padx=10)

        self.listbox_buku = tk.Listbox(self.frame_list, width=80, height=15)
        self.listbox_buku.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.frame_list, orient="vertical", command=self.listbox_buku.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox_buku.config(yscrollcommand=self.scrollbar.set)

        self.tampilkan_semua_buku() # Tampilkan buku saat aplikasi pertama kali dibuka

    def tambah_buku(self):
        """Menambahkan buku baru ke daftar dan memperbarui tampilan."""
        judul = self.entry_judul.get().strip()
        penulis = self.entry_penulis.get().strip()

        if not judul or not penulis:
            messagebox.showwarning("Input Kosong", "Judul dan Penulis tidak boleh kosong!")
            return

        buku_baru = {"judul": judul, "penulis": penulis}
        self.daftar_buku.append(buku_baru)
        messagebox.showinfo("Sukses", f"Buku '{judul}' oleh {penulis} berhasil ditambahkan!")
        self.clear_entries()
        self.tampilkan_semua_buku()

    def tampilkan_semua_buku(self):
        """Menampilkan semua buku yang ada di daftar ke Listbox."""
        self.listbox_buku.delete(0, tk.END) # Hapus item yang ada di listbox
        if not self.daftar_buku:
            self.listbox_buku.insert(tk.END, "Belum ada buku dalam daftar.")
            return

        for i, buku in enumerate(self.daftar_buku):
            self.listbox_buku.insert(tk.END, f"{i+1}. Judul: {buku['judul']}, Penulis: {buku['penulis']}")

    def cari_buku(self):
        """Mencari buku berdasarkan judul atau penulis dan menampilkan hasilnya."""
        kata_kunci = self.entry_judul.get().strip().lower() # Menggunakan entry judul sebagai input pencarian
        if not kata_kunci:
            messagebox.showwarning("Input Kosong", "Masukkan judul atau penulis untuk mencari.")
            return

        self.listbox_buku.delete(0, tk.END)
        ditemukan = False
        for i, buku in enumerate(self.daftar_buku):
            if kata_kunci in buku['judul'].lower() or kata_kunci in buku['penulis'].lower():
                self.listbox_buku.insert(tk.END, f"{i+1}. Judul: {buku['judul']}, Penulis: {buku['penulis']}")
                ditemukan = True
        
        if not ditemukan:
            self.listbox_buku.insert(tk.END, "Tidak ada buku yang cocok dengan kata kunci tersebut.")
        
        self.clear_entries()

    def hapus_buku(self):
        """Menghapus buku dari daftar berdasarkan pilihan di Listbox."""
        try:
            # Dapatkan indeks buku yang dipilih di listbox
            selected_index = self.listbox_buku.curselection()
            if not selected_index:
                messagebox.showwarning("Peringatan", "Pilih buku yang ingin dihapus terlebih dahulu.")
                return

            # Indeks yang dikembalikan oleh curselection adalah indeks Listbox (0-based)
            # Kita perlu mendapatkan indeks dari daftar_buku yang sebenarnya
            listbox_item_text = self.listbox_buku.get(selected_index[0])
            # Parse nomor buku dari teks item Listbox (misal: "1. Judul:...", ambil "1")
            buku_nomor_str = listbox_item_text.split('.')[0]
            indeks_buku_asli = int(buku_nomor_str) - 1 # Kurangi 1 karena indeks list Python dimulai dari 0

            if 0 <= indeks_buku_asli < len(self.daftar_buku):
                buku_terhapus = self.daftar_buku.pop(indeks_buku_asli)
                messagebox.showinfo("Sukses", f"Buku '{buku_terhapus['judul']}' berhasil dihapus.")
                self.tampilkan_semua_buku()
            else:
                messagebox.showerror("Error", "Indeks buku tidak valid.")
        except ValueError:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus buku.")
        except IndexError:
            messagebox.showerror("Error", "Pilih buku yang valid.")

    def clear_entries(self):
        """Mengosongkan kolom input judul dan penulis."""
        self.entry_judul.delete(0, tk.END)
        self.entry_penulis.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiBuku(root)
    root.mainloop()
