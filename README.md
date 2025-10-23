# 🏦 Sure Financial — AI Credit Card Statement Extractor# 🏦 Sure Financial — AI Credit Card Statement Extractor



> **Intelligent full-stack system** for parsing PDF credit card statements from 6 major Indian banks with AI-powered extraction and beautiful modern UI.> **Intelligent full-stack system** for parsing PDF credit card statements from 6 major Indian banks with AI-powered extraction and beautiful modern UI.



![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)

![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white)

![Tailwind](https://img.shields.io/badge/Tailwind-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white)

![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)![Tailwind](https://img.shields.io/badge/Tailwind-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

---![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)



## 🚀 Live Demo



- **Frontend**: [Deployed on Vercel](https://your-app.vercel.app) *(Add your URL)*---## ✨ Features

- **Backend API**: https://sure-financials-backend.onrender.com

- **API Documentation**: https://sure-financials-backend.onrender.com/docs



---## 🎯 Features- 🏦 **5 Banks Supported**: HDFC, ICICI, IDBI, SBI Card, Kotak Mahindra



## ✨ Features- 🤖 **AI-Powered**: Intelligent field extraction with confidence scoring



- 🏦 **6 Banks Supported**: HDFC, ICICI, IDBI, SBI Card, Kotak Mahindra, Axis Bank- ✅ **Multi-Bank Support**: HDFC, ICICI, IDBI, SBI, Kotak Mahindra- 📄 **OCR Ready**: Handles both digital and scanned PDFs

- 🤖 **AI-Powered Extraction**: Intelligent field detection with confidence scoring

- 📄 **OCR Ready**: Handles both digital and scanned PDFs (Tesseract)- ✅ **Smart Extraction**: Card number, billing cycle, due date, total amount due- 🎨 **Modern UI**: Beautiful gradient design with Tailwind CSS

- 🎨 **Modern UI**: Beautiful gradient design with Tailwind CSS

- 📊 **Multiple Formats**: JSON API + Excel downloads- ✅ **OCR Support**: Fallback for scanned PDFs (Tesseract)- 📊 **Multiple Formats**: JSON API + Excel downloads

- ⚡ **Lightning Fast**: Process statements in seconds

- 🔄 **Universal Parser**: Fallback for any bank statement- ✅ **Confidence Scoring**: AI-powered accuracy metrics- 🗄️ **Cloud Storage**: Optional Supabase integration

- 🎯 **95-100% Accuracy**: Tested on real bank statements

- ✅ **Excel Export**: Download results as XLSX- ⚡ **Lightning Fast**: Process statements in seconds

---

- ✅ **Batch Upload**: Process multiple PDFs or ZIP files

## 🏗️ Architecture

- ✅ **Modern UI**: Responsive design with drag-and-drop## 🚀 Quick Start

```

sure_financial/- ✅ **JSON/Table Toggle**: View data in multiple formats

├── backend/                    # FastAPI REST API

│   ├── main.py                # API endpoints (/upload, /extract)**Prerequisites**: Python 3.10+, Node.js 18+

│   ├── universal_parser.py    # Bank detection & routing

│   ├── parsers/               # Bank-specific extractors---

│   │   ├── hdfc_parser.py     # HDFC Bank parser

│   │   ├── icici_parser.py    # ICICI Bank parser### Backend

│   │   ├── idbi_parser.py     # IDBI Bank parser

│   │   ├── sbi_parser.py      # SBI Card parser## 🏗️ Architecture```powershell

│   │   ├── kotak_parser.py    # Kotak Mahindra parser

│   │   └── axis_parser.py     # Axis Bank parsercd backend

│   ├── utils/                 # Helper utilities

│   │   ├── pdf_utils.py       # 3-tier PDF extraction (pdfplumber → PyMuPDF → PyPDF2)```.\setup_env.ps1

│   │   ├── ocr_utils.py       # Tesseract OCR wrapper

│   │   └── data_formatter.py  # Amount/date cleaning (14 formats)sure_financial/. .\.venv\Scripts\Activate.ps1

│   └── requirements.txt       # Python dependencies

│├── backend/              # FastAPI REST APIpython -m uvicorn main:app --reload

└── frontend/                  # Next.js UI

    ├── pages/│   ├── main.py          # API endpoints```

    │   ├── index.js           # Landing page with features

    │   └── upload.js          # Upload interface with results│   ├── universal_parser.py  # Bank detection & parsing

    ├── components/            # React components

    │   ├── FileUploader.jsx   # Drag-and-drop uploader│   ├── parsers/         # Bank-specific parsersBackend runs at: http://localhost:8000

    │   ├── DataTable.jsx      # Table view with confidence bars

    │   ├── JsonViewer.jsx     # JSON viewer with copy│   │   ├── hdfc_parser.py

    │   └── Loader.jsx         # Loading animation

    └── package.json           # Node dependencies│   │   ├── icici_parser.py### Frontend

```

│   │   ├── idbi_parser.py```powershell

---

│   │   ├── sbi_parser.pycd frontend

## 🚀 Quick Start (Local Development)

│   │   └── kotak_parser.pynpm install

### Prerequisites

- **Python 3.10+**│   └── utils/           # Helper utilitiesnpm run dev

- **Node.js 18+**

- **Tesseract OCR** (Optional, for scanned PDFs)│       ├── pdf_utils.py```



### 1. Clone Repository│       ├── ocr_utils.py



```bash│       └── data_formatter.pyFrontend runs at: http://localhost:3000

git clone https://github.com/Shobit04/sure_financial.git

cd sure_financial│

```

└── frontend/            # Next.js UI## 📖 Documentation

### 2. Backend Setup

    ├── pages/

```powershell

# Navigate to backend    │   ├── index.js     # Landing page- **[Complete Setup Guide](SETUP_GUIDE.md)** - Step-by-step installation

cd backend

    │   └── upload.js    # Upload interface- **[Backend README](backend/README.md)** - API documentation

# Create virtual environment

python -m venv .venv    └── components/- **[Frontend README](frontend/README.md)** - UI customization



# Activate virtual environment        ├── FileUploader.jsx

.\.venv\Scripts\Activate.ps1

        ├── DataTable.jsx## 📁 Project Structure

# Install dependencies

pip install -r requirements.txt        ├── JsonViewer.jsx



# (Optional) Configure OCR - create .env file        └── Loader.jsx```

# TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe

```sure_financial/

# Run backend

python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000├── backend/              # FastAPI Python backend

```

---│   ├── main.py          # API endpoints

**Backend runs at**: http://localhost:8000  

**API Docs**: http://localhost:8000/docs│   ├── universal_parser.py



### 3. Frontend Setup## 🚀 Quick Start│   ├── parsers/         # Bank-specific extractors



```powershell│   ├── utils/           # PDF, OCR, Supabase utilities

# Open new terminal, navigate to frontend

cd frontend### Prerequisites│   └── requirements.txt



# Install dependencies│

npm install

- **Python 3.10+** - [Download](https://www.python.org/downloads/)└── frontend/            # Next.js + Tailwind UI

# Create .env.local for local development

# NEXT_PUBLIC_API_URL=http://localhost:8000- **Node.js 18+** - [Download](https://nodejs.org/)    ├── pages/           # Route pages



# Run frontend- **Tesseract OCR** (Optional) - [Download](https://github.com/UB-Mannheim/tesseract/wiki)    ├── components/      # React components

npm run dev

```    └── styles/          # Tailwind CSS



**Frontend runs at**: http://localhost:3000### 1. Clone Repository```



---



## 🏦 Supported Banks```bash## 🎯 What It Extracts



| Bank | Card Type | Detection Keywords | Test Results | Confidence |git clone <your-repo-url>

|------|-----------|-------------------|--------------|------------|

| **HDFC Bank** | Credit | "HDFC", "HDFC Bank" | ✅ 100% on real statements | 95-100% |cd sure_financialFrom any supported bank statement:

| **ICICI Bank** | Credit | "ICICI", "ICICI Bank" | ✅ Tested | 90-100% |

| **IDBI Bank** | Credit | "IDBI", "Industrial Development Bank" | ✅ Tested | 85-100% |```

| **SBI Card** | Credit | "State Bank", "SBI Card" | ✅ Tested | 90-100% |

| **Kotak Mahindra** | Credit | "Kotak", "Kotak Mahindra" | ✅ Tested | 90-100% |1. ✅ **Bank Name** / Card Provider

| **Axis Bank** | Credit | "Axis Bank", "Axis" | ✅ 100% on real statements | 95-100% |

### 2. Setup Backend2. ✅ **Card Last 4 Digits**

---

3. ✅ **Billing Cycle** Period

## 📊 Extracted Fields

```powershell4. ✅ **Payment Due Date**

From any supported bank statement:

# Navigate to backend5. ✅ **Total Outstanding Amount**

1. ✅ **Bank Name** - Auto-detected from PDF content

2. ✅ **Card Last 4 Digits** - e.g., "5692"cd backend

3. ✅ **Billing Cycle** - e.g., "14 Aug 2025 - 12 Sep 2025"

4. ✅ **Payment Due Date** - e.g., "2025-10-03"Plus: Confidence score, AI summary, and validation notes.

5. ✅ **Total Amount Due** - e.g., "₹11,532.82"

# Create virtual environment

**Plus**: Confidence score (0-1.0), AI-generated summary, and validation notes

python -m venv .venv## 🛠️ Tech Stack

---



## 📋 API Endpoints

# Activate virtual environment**Backend**

### `POST /extract`

Extract data from a single PDF statement..\.venv\Scripts\Activate.ps1- FastAPI - Modern Python web framework



**Request:**- PyMuPDF, pdfplumber - PDF parsing

```bash

curl -X POST https://sure-financials-backend.onrender.com/extract \# Install dependencies- Pytesseract - OCR for scanned PDFs

  -F "file=@statement.pdf"

```pip install -r requirements.txt- Pandas - Data processing



**Response:**- Supabase - Cloud storage (optional)

```json

{# Configure environment (optional for OCR)

  "bank": "HDFC Bank",

  "card_last_4": "5692",copy .env.example .env**Frontend**

  "billing_cycle": "09 Sep 2025 - 09 Oct 2025",

  "payment_due_date": "2025-10-27",# Edit .env and set TESSERACT_CMD path if using OCR- Next.js 14 - React framework

  "total_due": "₹61.00",

  "confidence": 1.0,```- Tailwind CSS - Utility-first styling

  "summary": "Your HDFC Bank credit card statement shows a total due of ₹61.00..."

}- Axios - HTTP client

```

### 3. Setup Frontend- Modern responsive design

**Excel Export:**

```bash

curl -X POST https://sure-financials-backend.onrender.com/extract \

  -F "file=@statement.pdf" \```powershell## 📸 Screenshots

  -F "as_excel=true" \

  -o extraction.xlsx# Navigate to frontend

```

cd ..\frontend- **Landing Page**: Gradient hero with feature cards

### `POST /upload`

Upload multiple PDFs (supports ZIP files).- **Upload Page**: Drag-and-drop with live preview



**Request:**# Install dependencies- **Results View**: JSON/Table toggle with confidence meter

```bash

curl -X POST https://sure-financials-backend.onrender.com/upload \npm install- **Responsive**: Works on all devices

  -F "file=@statements.zip"

``````



**Response:**## 🧪 API Endpoints

```json

{### 4. Run Application

  "job_id": "job_1729689600",

  "files": ["hdfc_statement.pdf", "axis_statement.pdf"]### `POST /extract`

}

```**Terminal 1 - Backend:**Upload PDF and get extracted JSON



---```powershell



## 🎨 Frontend Featurescd D:\sure_financial\backend### `POST /upload`



### Landing Page (`/`).\.venv\Scripts\Activate.ps1Batch upload (ZIP support)

- Overview of features and supported banks

- Gradient hero section with call-to-actionpython -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

- Feature cards with icons

- Responsive design```### `GET /history`



### Upload Page (`/upload`)Retrieve extraction history (requires Supabase)

- **Drag & Drop**: Easy file upload with visual feedback

- **JSON Viewer**: Copy extracted data to clipboard**Terminal 2 - Frontend:**

- **Table View**: Formatted display with confidence bars

- **Excel Download**: Export results instantly```powershellSee `backend/README.md` for full API docs.

- **Real-time Processing**: Live progress indicators

- **Error Handling**: Clear error messages with suggestionscd D:\sure_financial\frontend



---npm run dev## 🔧 Configuration



## 🔧 Configuration```



### Backend Environment Variables**Backend** (`backend/.env`):



Optional - create `backend/.env`:**Open Browser:**```env



```bash- Frontend: http://localhost:3000TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe

# Tesseract OCR path (optional, for scanned PDFs)

TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe- Backend API Docs: http://localhost:8000/docsSUPABASE_URL=https://your-project.supabase.co

```

SUPABASE_KEY=your-key

### Frontend Environment Variables

---```

**Local Development** (`frontend/.env.local`):

```bash

NEXT_PUBLIC_API_URL=http://localhost:8000

```## 📋 API Endpoints**Frontend**: Update API URL in `pages/upload.js`



**Production** (Set in Vercel):

```bash

NEXT_PUBLIC_API_URL=https://sure-financials-backend.onrender.com### `POST /upload`## 🚀 Deployment

```

Upload multiple PDFs or ZIP file for batch processing.

---

- **Backend**: Render, Railway, Fly.io

## 🚢 Deployment

**Request:**- **Frontend**: Vercel, Netlify

### Backend (Render)

```bash- **Database**: Supabase Cloud

1. Go to [Render Dashboard](https://dashboard.render.com/)

2. New → Web Service → Connect GitHub repocurl -X POST http://localhost:8000/upload \

3. Configure:

   - **Root Directory**: `backend`  -F "file=@statements.zip"See deployment guides in respective README files.

   - **Build Command**: `pip install -r requirements.txt`

   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT````

4. Deploy

## 📈 Future Enhancements

### Frontend (Vercel)

**Response:**

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)

2. New Project → Import GitHub repo```json- [ ] Transaction table extraction

3. Configure:

   - **Root Directory**: `frontend`{- [ ] Month-over-month spending analysis

   - **Framework**: Next.js (auto-detected)

4. Add Environment Variable:  "job_id": "job_1729689600",- [ ] Chat-based queries

   - `NEXT_PUBLIC_API_URL` = `https://sure-financials-backend.onrender.com`

5. Deploy  "files": ["hdfc_statement.pdf", "icici_statement.pdf"]- [ ] Email integration (Gmail API)



**Auto-Deploy**: Both platforms automatically redeploy when you push to GitHub!}- [ ] Multi-language support



For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).```- [ ] Mobile apps



---



## 🧪 Testing### `POST /extract`## 🤝 Contributing



### Test Backend APIExtract data from a single PDF.



```powershellContributions welcome! Fork, create a feature branch, and submit a PR.

# Check API health

curl https://sure-financials-backend.onrender.com/docs**Request:**



# Test extraction with sample PDF```bash## 📄 License

curl -X POST https://sure-financials-backend.onrender.com/extract \

  -F "file=@sample_statement.pdf"curl -X POST http://localhost:8000/extract \

```

  -F "file=@statement.pdf" \MIT License

### Test Frontend

  -F "as_excel=false"

1. Open your Vercel URL in browser

2. Navigate to Upload page```---

3. Drag & drop a PDF statement

4. Verify extraction results display correctly



---**Response:****Built with ❤️ for financial automation**



## 🛠️ Tech Stack```json



### Backend{For detailed setup instructions, see **[SETUP_GUIDE.md](SETUP_GUIDE.md)**

- **FastAPI 0.95.2** - Modern Python web framework

- **pdfplumber 0.7.6** - Primary PDF text extraction  "bank": "HDFC Bank",

- **PyMuPDF 1.22.5** - Secondary PDF extraction

- **PyPDF2 3.0.1** - Fallback PDF extraction  "card_last_4": "1234",

- **pytesseract 0.3.10** - OCR for scanned PDFs  "billing_cycle": "01 Sep 2025 - 30 Sep 2025",

- **pandas 2.2.3** - Data manipulation  "payment_due_date": "2025-10-15",

- **openpyxl 3.1.2** - Excel export  "total_due": "₹25,340.75",

  "confidence": 0.95,

### Frontend  "summary": "Your HDFC Bank credit card statement..."

- **Next.js 14.0.0** - React framework with SSR}

- **Tailwind CSS** - Utility-first styling```

- **Axios** - HTTP client for API calls

- **React** - UI library**Excel Export:**

```bash

### Deploymentcurl -X POST http://localhost:8000/extract \

- **Render** - Backend hosting (Python)  -F "file=@statement.pdf" \

- **Vercel** - Frontend hosting (Next.js)  -F "as_excel=true" \

- **GitHub** - Version control and CI/CD  -o extraction.xlsx

```

---

---

## 🔍 How It Works

## 🎨 Frontend Usage

1. **PDF Upload**: User uploads credit card statement (PDF)

2. **Bank Detection**: System analyzes text to identify bank### 1. Landing Page (/)

3. **Parser Selection**: Routes to bank-specific parser (6 available)- Overview of features

4. **Data Extraction**: Regex patterns extract key fields- Supported banks

5. **Validation**: Cleans amounts, validates dates (14 formats)- Getting started guide

6. **Confidence Scoring**: Calculates accuracy based on fields found

7. **Response**: Returns JSON with extracted data + confidence### 2. Upload Page (/upload)

8. **Excel Export**: Optional XLSX download- Drag & drop PDF file

- View results in JSON or Table format

### Extraction Confidence Levels- Download as Excel

- Confidence meter for accuracy

- **95-100%**: All fields extracted successfully

- **75-94%**: Most fields found, minor gaps### Features:

- **50-74%**: Partial extraction, manual review suggested- **Drag & Drop**: Easy file upload

- **0-49%**: Low confidence, check original PDF- **JSON Viewer**: Copy extracted data

- **Table View**: Formatted display with confidence bars

---- **Excel Download**: Export results instantly

- **Responsive Design**: Works on mobile, tablet, desktop

## 🔧 Development

---

### Adding a New Bank Parser

## 🔧 Configuration

1. **Create Parser File**: `backend/parsers/newbank_parser.py`

### Backend (.env)

```python

import re```bash

from utils.data_formatter import clean_amount, clean_date# Tesseract OCR path (optional, for scanned PDFs)

TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe

class NewBankParser:

    def extract(self, text: str) -> dict:# Temporary cache path

        return {TEMP_DB_PATH=./tmp_cache.db

            'card_last_4': self._extract_card(text),```

            'billing_cycle': self._extract_cycle(text),

            'payment_due_date': self._extract_due_date(text),### Frontend

            'total_due': self._extract_total(text)

        }API endpoint configured in `pages/upload.js`:

    ```javascript

    def _extract_card(self, text: str) -> str:const apiUrl = 'http://localhost:8000/extract';

        match = re.search(r'Card No\.\s*[X\s]*(\d{4})', text)```

        return match.group(1) if match else None

    For production, update to your deployed backend URL.

    # Implement other extraction methods...

```---



2. **Register in Universal Parser**: `backend/universal_parser.py`## 🏦 Supported Banks



```python| Bank | Detection Keywords | Confidence Factors |

from parsers.newbank_parser import NewBankParser|------|-------------------|-------------------|

| **HDFC Bank** | "HDFC", "HDFC Bank" | Card number, due date, total due |

# Add to detect_bank method| **ICICI Bank** | "ICICI", "ICICI Bank" | Payment due, statement period |

if 'NEW BANK' in text_upper:| **IDBI Bank** | "IDBI", "Industrial Development Bank" | Account summary, billing cycle |

    return 'New Bank'| **SBI** | "State Bank", "SBI Card" | Due date, minimum amount due |

| **Kotak Mahindra** | "Kotak", "Kotak Mahindra" | Credit card number, payment date |

# Add to parser_map

'New Bank': NewBankParser()---

```

## 📊 Data Extraction

3. **Test with real statements** and update README

### Fields Extracted:

---

1. **Bank Name**: Auto-detected from PDF content

## 📁 Project Files2. **Card Last 4 Digits**: e.g., "1234"

3. **Billing Cycle**: e.g., "01 Sep 2025 - 30 Sep 2025"

### Core Files4. **Payment Due Date**: e.g., "2025-10-15"

- `backend/main.py` - FastAPI application entry point5. **Total Amount Due**: e.g., "₹25,340.75"

- `backend/universal_parser.py` - Bank detection and parser routing

- `frontend/pages/upload.js` - Main upload interface### Confidence Scoring:

- `requirements.txt` - Python dependencies

- `package.json` - Node dependencies- **95-100%**: All fields extracted with high certainty

- **75-94%**: Most fields found, minor gaps

### Documentation- **50-74%**: Partial extraction, manual review suggested

- `README.md` - This file- **0-49%**: Low confidence, check original PDF

- `DEPLOYMENT.md` - Detailed deployment guide

- `DEPLOY_COMMANDS.md` - Quick reference commands---

- `READY_TO_DEPLOY.md` - Pre-deployment checklist

## 🧪 Testing

### Configuration

- `.gitignore` - Excludes venv, node_modules, .env, uploads### Test Backend:

- `.env.example` - Example environment variables

- `backend/.env` - Backend configuration (optional)```powershell

- `frontend/.env.local` - Frontend configuration (local)# Test API health

curl http://localhost:8000/docs

---

# Test extraction with sample PDF

## 🔍 Troubleshootingcurl -X POST http://localhost:8000/extract \

  -F "file=@sample_statement.pdf"

### Backend Issues```



**Port 8000 already in use:**### Test Frontend:

```powershell

netstat -ano | findstr :80001. Start frontend: `npm run dev`

taskkill /PID <PID> /F2. Open: http://localhost:3000

```3. Go to Upload page

4. Drag & drop a test PDF

**Module not found:**5. Verify results display

```powershell

cd backend---

pip install -r requirements.txt --force-reinstall

```## 🔍 Troubleshooting



**Render deployment fails:**### Backend Won't Start

- Check build logs for errors

- Verify `requirements.txt` syntax```powershell

- Ensure Python 3.10+ compatibility# Check if port 8000 is in use

netstat -ano | findstr :8000

### Frontend Issues

# Kill process if needed

**API connection fails:**taskkill /PID <PID> /F

- Verify `NEXT_PUBLIC_API_URL` is set in Vercel

- Check CORS configuration in `backend/main.py`# Reinstall dependencies

- Inspect Network tab in browser console (F12)cd backend

pip install -r requirements.txt --force-reinstall

**Build fails on Vercel:**```

- Check `package.json` for missing dependencies

- Verify Node.js version compatibility (18+)### Frontend Won't Start

- Review build logs for specific errors

```powershell

### Low Confidence Scores# Clean install

cd frontend

- **Check PDF Quality**: Ensure text is readable and not password-protectedRemove-Item -Recurse -Force node_modules

- **Use OCR**: Install Tesseract for scanned documentsnpm cache clean --force

- **Manual Review**: Compare extracted data with original PDFnpm install

- **Update Parsers**: Enhance regex patterns for specific bank formatsnpm run dev

```

---

### OCR Not Working

## 📄 License

1. **Install Tesseract OCR**: [Download Here](https://github.com/UB-Mannheim/tesseract/wiki)

MIT License - feel free to use for personal or commercial projects.2. **Set Path in .env**:

   ```bash

---   TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe

   ```

## 🤝 Contributing3. **Restart Backend**



Contributions welcome!### Low Confidence Scores



1. Fork the repository- **Check PDF Quality**: Ensure text is readable

2. Create feature branch: `git checkout -b feature/new-parser`- **Use OCR**: For scanned documents, install Tesseract

3. Commit changes: `git commit -m 'Add parser for XYZ Bank'`- **Manual Review**: Check extracted fields vs original PDF

4. Push to branch: `git push origin feature/new-parser`- **Update Parsers**: Enhance regex patterns in `parsers/`

5. Open Pull Request

---

---

## 🛠️ Development

## 📞 Support

### Adding a New Bank

**Having issues?**

1. **Create Parser**: `backend/parsers/your_bank_parser.py`

1. Check [Troubleshooting](#-troubleshooting) section above

2. Review backend logs in Render dashboard```python

3. Check frontend console (F12) in browserimport re

4. Read [DEPLOYMENT.md](DEPLOYMENT.md) for deployment issuesfrom utils.data_formatter import clean_amount, clean_date

5. Create an issue on GitHub

class YourBankParser:

---    def extract(self, text: str) -> dict:

        return {

## 🎯 Future Enhancements            'card_last_4': self._extract_card(text),

            'billing_cycle': self._extract_cycle(text),

- [ ] Transaction table extraction            'payment_due_date': self._extract_due_date(text),

- [ ] Month-over-month spending analysis            'total_due': self._extract_total(text)

- [ ] Email integration (Gmail API)        }

- [ ] Mobile app (React Native)    

- [ ] Multi-language support    def _extract_card(self, text: str) -> str:

- [ ] More banks (Yes Bank, IndusInd, etc.)        match = re.search(r'XXXX\s*XXXX\s*XXXX\s*(\d{4})', text)

- [ ] PDF password unlock        return match.group(1) if match else None

- [ ] Batch processing improvements    

    # Implement other extraction methods...

---```



## 🙏 Acknowledgments2. **Register in Universal Parser**: `backend/universal_parser.py`



Built with ❤️ using:```python

- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web frameworkfrom parsers.your_bank_parser import YourBankParser

- [Next.js](https://nextjs.org/) - React framework for production

- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSSdef detect_bank(self, text: str) -> str:

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - OCR engine    if 'YOUR BANK' in text.upper():

- [Render](https://render.com/) - Backend hosting        return 'Your Bank'

- [Vercel](https://vercel.com/) - Frontend hosting    # ... existing banks

```

---

3. **Add to Bank List**: Update README.md supported banks section

**🚀 Built for financial automation and AI-powered data extraction**

### Enhancing UI

**GitHub**: https://github.com/Shobit04/sure_financial  

**Live Demo**: [View Application](https://your-app.vercel.app)Frontend uses Tailwind CSS. Customize in:

- `tailwind.config.js` - Theme colors, fonts

---- `styles/globals.css` - Global styles

- Components in `components/` - Reusable UI elements

*Last Updated: October 2025*

---

## 📦 Dependencies

### Backend

- **fastapi** - REST API framework
- **uvicorn** - ASGI server
- **pdfplumber** - PDF text extraction
- **PyMuPDF** - PDF rendering
- **pytesseract** - OCR engine wrapper
- **pandas** - Data manipulation
- **openpyxl** - Excel export

### Frontend

- **Next.js** - React framework
- **Tailwind CSS** - Utility-first CSS
- **axios** - HTTP client
- **React** - UI library

---

## 🚢 Deployment

### Backend (FastAPI)

**Option 1: Docker**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Option 2: Railway/Render/Heroku**
- Set buildpack to Python
- Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Frontend (Next.js)

**Option 1: Vercel** (Recommended)
```bash
npm install -g vercel
vercel
```

**Option 2: Static Export**
```bash
npm run build
npm run export
# Deploy `out/` folder to any static host
```

**Update API URL** in production:
```javascript
// frontend/pages/upload.js
const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/extract';
```

---

## 📄 License

MIT License - feel free to use for personal or commercial projects.

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-bank-parser`
3. Commit changes: `git commit -m 'Add parser for XYZ Bank'`
4. Push to branch: `git push origin feature/new-bank-parser`
5. Open a Pull Request

---

## 📞 Support

Having issues? Check:

1. **Troubleshooting section** above
2. **Backend logs** in terminal
3. **Frontend console** (F12 in browser)
4. **API docs** at http://localhost:8000/docs

---

## 🎉 Credits

Built with ❤️ using:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Next.js](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

---

**🚀 Ready to extract? Start the servers and upload your first PDF!**
