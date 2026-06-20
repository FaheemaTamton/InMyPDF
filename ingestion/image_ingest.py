

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
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
