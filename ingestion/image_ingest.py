import pytesseract
from PIL import Image
import pdfplumber
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_images_text(pdf_path) -> str:
    image_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:s
            for image in page.images:
                cropped = page.crop((
                    image["x0"],
                    image["top"],
                    image["x1"],
                    image["bottom"]
                ))

                img = cropped.to_image(resolution=300).original
                text = pytesseract.image_to_string(img)
                image_text += text + "\n"

    return image_text
