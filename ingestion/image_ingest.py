import pytesseract
from PIL import Image
import pdfplumber
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_images_text(pdf_path) -> str:
    image_text = ""

