import os
import io
import zipfile
import tempfile
import json
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import pandas as pd

from utils.pdf_utils import extract_text_from_pdf
from utils.ocr_utils import ocr_pdf_to_text
from universal_parser import UniversalParser

load_dotenv()

app = FastAPI(title="Card Statement Extractor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

parser = UniversalParser()


@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    """Accept PDF or ZIP of PDFs. Returns a job id and basic metadata."""
    if not (file.filename.lower().endswith('.pdf') or file.filename.lower().endswith('.zip')):
        raise HTTPException(status_code=400, detail='Only PDF or ZIP uploads allowed')

    tmpdir = tempfile.mkdtemp()
    saved_paths = []

    contents = await file.read()
    if file.filename.lower().endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(contents)) as z:
            for name in z.namelist():
                if name.lower().endswith('.pdf'):
                    outpath = os.path.join(tmpdir, os.path.basename(name))
                    with open(outpath, 'wb') as f:
                        f.write(z.read(name))
                    saved_paths.append(outpath)
    else:
        outpath = os.path.join(tmpdir, file.filename)
        with open(outpath, 'wb') as f:
            f.write(contents)
        saved_paths.append(outpath)

    # For prototype, return list of files saved and a temporary id
    job_id = f"job_{int(datetime.utcnow().timestamp())}"
    return {"job_id": job_id, "files": [os.path.basename(p) for p in saved_paths]}


@app.post('/extract')
async def extract(file: UploadFile = File(...), as_excel: bool = Form(False)):
    """Extract key fields from uploaded PDF and return JSON (and Excel if requested)."""
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail='Only PDF uploads allowed for extraction')

    contents = await file.read()
    # write to temp
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    # Try text extraction via PDF parsers first (for digital PDFs)
    text = extract_text_from_pdf(tmp_path)
    
    # If no text extracted or very little text, fallback to OCR (for scanned PDFs)
    if not text or len(text.strip()) < 50:
        try:
            text = ocr_pdf_to_text(tmp_path)
            if text and len(text.strip()) >= 50:
                result = parser.parse_text(text)
                result['extraction_method'] = 'OCR (scanned PDF)'
            else:
                raise HTTPException(status_code=400, detail='Unable to extract text from PDF. Please ensure the PDF is readable and not corrupted.')
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'OCR failed: {str(e)}. Please check if Tesseract is installed.')
    else:
        result = parser.parse_text(text)
        result['extraction_method'] = 'Text extraction (digital PDF)'

    # store in pandas for Excel export
    df = pd.DataFrame([result])

    if as_excel:
        output = io.BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        filename = f"extraction_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.xlsx"
        return StreamingResponse(output, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers={"Content-Disposition": f"attachment; filename={filename}"})

    return JSONResponse(result)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
