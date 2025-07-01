import pytesseract
from PIL import Image
import sys as sp
import os

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan!"
    return a / b

def ekstrak_ekspresi_dari_gambar(file_path):
    try:
        if not os.path.exists(file_path):
            return None, "Error: File tidak ditemukan!"
        if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            return None, "Error: Format file harus PNG atau JPG!"
        
        img = Image.open(file_path)
        img = img.convert('L')
        teks = pytesseract.image_to_string(img).strip()
        allowed_chars = set('0123456789 +-*/.')
        if not teks or not all(c in allowed_chars for c in teks):
            return None, f"Error: Ekspresi tidak valid atau tidak terdeteksi: {teks}"
        
        return teks, None
    except Exception as e:
        return None, f"Error saat memproses gambar: {e}"

def evaluasi_ekspresi(ekspresi):
    try:
        ekspresi = ekspresi.replace('x', '*')
        hasil = sp.sympify(ekspresi)
        return hasil, None
    except Exception as e:
        return None, f"Error: Ekspresi matematika tidak valid: {e}"

def kalkulator_manual():
    print("=== Kalkulator Aritmatika Dasar ===")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    
    try:
        pilihan = int(input("Masukkan pilihan (1-4): "))
        if pilihan not in [1, 2, 3, 4]:
            print("Pilihan tidak valid!")
            return
        
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        
        if pilihan == 1:
            hasil = tambah(a, b)
            print(f"Hasil: {a} + {b} = {hasil}")
        elif pilihan == 2:
            hasil = kurang(a, b)
            print(f"Hasil: {a} - {b} = {hasil}")
        elif pilihan == 3:
            hasil = kali(a, b)
            print(f"Hasil: {a} * {b} = {hasil}")
        elif pilihan == 4:
            hasil = bagi(a, b)
            print(f"Hasil: {a} / {b} = {hasil}")
            
    except ValueError:
        print("Error: Masukkan angka yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def kalkulator_foto():
    print("=== Kalkulator Berbasis Foto ===")
    file_path = input("Masukkan path file gambar (contoh: soal.png): ").strip()
    ekspresi, error = ekstrak_ekspresi_dari_gambar(file_path)
    if error:
        print(error)
        return
    
    print(f"Ekspresi terdeteksi: {ekspresi}")
    hasil, error = evaluasi_ekspresi(ekspresi)
    if error:
        print(error)
        return
    
    print(f"Hasil: {ekspresi} = {hasil}")

def main():
    while True:
        print("\n=== Kalkulator Aritmatika ===")
        print("1. Kalkulator Manual")
        print("2. Kalkulator Berbasis Foto")
        print("3. Keluar")
        
        try:
            pilihan = int(input("Masukkan pilihan (1-3): "))
            if pilihan == 1:
                kalkulator_manual()
            elif pilihan == 2:
                kalkulator_foto()
            elif pilihan == 3:
                print("Terima kasih telah menggunakan kalkulator!")
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Error: Masukkan angka yang valid!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
