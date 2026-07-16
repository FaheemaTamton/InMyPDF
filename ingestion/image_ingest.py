import pytesseract
from PIL import Image
import pdfplumber
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"




                img = cropped.to_image(resolution=300).original
                text = pytesseract.image_to_string(img)
                image_text += text + "\n"

    return image_text
