from pdf2image import convert_from_path
import pytesseract


pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pdf_to_text(pdf_path: str) -> str:
    pages = convert_from_path(pdf_path, poppler_path=r"C:\Users\kausa\OneDrive\Documents\personal\Release-25.12.0-0\poppler-25.12.0\Library\bin")

    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)

    return text