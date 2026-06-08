import fitz  # PyMuPDF
import sys
sys.stdout.reconfigure(encoding='utf-8')

def extract_text(pdf_path, max_pages=30):
    try:
        doc = fitz.open(pdf_path)
        text = f"--- Extracted from {pdf_path} ---\n"
        for i in range(min(max_pages, len(doc))):
            page = doc.load_page(i)
            text += page.get_text() + "\n"
        return text
    except Exception as e:
        return f"Error extracting from {pdf_path}: {e}\n"

if __name__ == "__main__":
    paths = [
        "resources/ISLR_First_Printing.pdf",
        "resources/Deep Learning with Python.pdf"
    ]
    for p in paths:
        print(extract_text(p, 40)[:2000]) # Print first 2000 chars of extracted text to avoid too much output
        print("\n\n" + "="*50 + "\n\n")
