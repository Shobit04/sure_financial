import os
from typing import List
from PIL import Image
import pytesseract
import fitz


def ocr_pdf_to_text(path: str) -> str:
    """
    Render each PDF page to an image and OCR with pytesseract.
    Works with scanned PDFs or image-based PDFs.
    Requires Tesseract OCR to be installed.
    """
    texts: List[str] = []

    # Allow user to set TESSERACT_CMD via env
    tcmd = os.getenv('TESSERACT_CMD')
    if tcmd and os.path.exists(tcmd):
        pytesseract.pytesseract.tesseract_cmd = tcmd
    
    # Check if Tesseract is available
    try:
        pytesseract.get_tesseract_version()
    except Exception:
        raise Exception(
            "Tesseract OCR not found. Please install Tesseract and set TESSERACT_CMD in .env file. "
            "Download from: https://github.com/UB-Mannheim/tesseract/wiki"
        )

    try:
        doc = fitz.open(path)
        for page_num, page in enumerate(doc):
            # Render page at higher DPI for better OCR accuracy
            pix = page.get_pixmap(dpi=300)  # Increased from 200 to 300 DPI
            img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
            
            # OCR with language and configuration options
            text = pytesseract.image_to_string(
                img, 
                lang='eng',
                config='--psm 6'  # Assume uniform block of text
            )
            
            if text and text.strip():
                texts.append(text)
                
    except Exception as e:
        raise Exception(f"OCR processing failed: {str(e)}")

    if not texts:
        raise Exception("No text could be extracted from the PDF using OCR")

    return "\n\n".join(texts)
