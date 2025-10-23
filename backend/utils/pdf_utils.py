import fitz  # PyMuPDF
import pdfplumber
import PyPDF2
from typing import List


def extract_text_from_pdf(path: str) -> str:
    """
    Try multiple PDF libraries to extract text robustly.
    Works with digital PDFs that have embedded text.
    Falls back to multiple libraries for maximum compatibility.
    """
    texts: List[str] = []

    # Method 1: Try pdfplumber (best for structured PDFs)
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t and t.strip():
                    texts.append(t)
        if texts:
            return "\n\n".join(texts)
    except Exception:
        pass

    # Method 2: Try PyMuPDF (good for most PDFs)
    try:
        doc = fitz.open(path)
        for page in doc:
            t = page.get_text()
            if t and t.strip():
                texts.append(t)
        if texts:
            return "\n\n".join(texts)
    except Exception:
        pass

    # Method 3: Try PyPDF2 (fallback for problematic PDFs)
    try:
        with open(path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                t = page.extract_text()
                if t and t.strip():
                    texts.append(t)
        if texts:
            return "\n\n".join(texts)
    except Exception:
        pass

    # If all methods failed, return empty string
    # This will trigger OCR fallback in main.py
    return ""
