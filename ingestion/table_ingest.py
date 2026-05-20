import pdfplumber

def extract_tables(pdf_path) -> str:
    tables_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    tables_text += " | ".join(cell or "" for cell in row) + "\n"
                tables_text += "\n"

    return tables_text
