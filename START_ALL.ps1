# 🚀 Sure Financial - Quick Start Script

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "� SURE FINANCIAL - Starting All Services" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

$projectRoot = "D:\sure_financial"
Set-Location $projectRoot

# Start Backend
Write-Host "� Starting Backend (Port 8000)..." -ForegroundColor Yellow
$backend = Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd D:\sure_financial\backend; .\.venv\Scripts\Activate.ps1; python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000" -PassThru
Write-Host "✅ Backend started (PID: $($backend.Id))" -ForegroundColor Green

Start-Sleep -Seconds 5

# Start Frontend
Write-Host "🎨 Starting Frontend (Port 3000)..." -ForegroundColor Yellow
$frontend = Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd D:\sure_financial\frontend; npm run dev" -PassThru
Write-Host "✅ Frontend started (PID: $($frontend.Id))" -ForegroundColor Green

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "✅ ALL SERVICES RUNNING!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Access Points:" -ForegroundColor Cyan
Write-Host "   • Frontend:  http://localhost:3000" -ForegroundColor White
Write-Host "   • Backend:   http://localhost:8000" -ForegroundColor White
Write-Host "   • API Docs:  http://localhost:8000/docs" -ForegroundColor White
Write-Host ""
Write-Host "📖 Documentation: README.md" -ForegroundColor Cyan
Write-Host ""

Start-Sleep -Seconds 8
Write-Host "🌐 Opening browser..." -ForegroundColor Cyan
Start-Process "http://localhost:3000"

Write-Host ""
Write-Host "✨ Ready! Upload your first PDF statement! ✨" -ForegroundColor Green
Write-Host ""
