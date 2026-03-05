import sys
import pdfplumber

def check_pdf(path):
    try:
        with pdfplumber.open(path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            print(f"Total pages: {len(pdf.pages)}")
            print(f"Total characters: {len(text)}")
    except Exception as e:
        print(f"Error: {e}")

check_pdf(r"d:\桌面\DZ10003\EPCO总承包合同2025.12.16.pdf")
