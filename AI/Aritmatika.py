import pytesseract
from PIL import Image
import re

# Path ke executable Tesseract (hanya diperlukan di Windows, sesuaikan path-nya)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        # Buka gambar menggunakan Pillow
        image = Image.open(image_path)
        
        # Ekstrak teks dari gambar menggunakan pytesseract
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {e}"

def calculate_expression(text):
    try:
        # Cari ekspresi aritmatika menggunakan regex (misalnya: 2 + 3, 5 * 4, dll.)
        pattern = r'(\d+\s*[\+\-\*/]\s*\d+)'
        match = re.search(pattern, text)
        
        if not match:
            return "No valid arithmetic expression found."
        
        expression = match.group(0)
        # Evaluasi ekspresi aritmatika (hati-hati dengan eval, gunakan hanya untuk input terpercaya)
        result = eval(expression)
        return f"Expression: {expression} = {result}"
    except Exception as e:
        return f"Error calculating expression: {e}"

def main(image_path):
    # Ekstrak teks dari gambar
    text = extract_text_from_image(image_path)
    print("Extracted Text:", text)
    
    # Hitung ekspresi aritmatika dari teks
    result = calculate_expression(text)
    print(result)

# Contoh penggunaan
if __name__ == "__main__":
    # Ganti dengan path ke gambar Anda
    image_path = "path_to_your_image.jpg"  # Misalnya, gambar berisi teks "2 + 3"
    main(image_path)