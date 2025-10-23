<#
Create Python virtual environment and install requirements (Windows PowerShell)
#>
$ErrorActionPreference = 'Stop'

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python is not found in PATH. Please install Python 3.10+ and ensure 'python' is in PATH."
    exit 1
}

python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Virtualenv created at .\.venv and packages installed. Activate with: . .\\.venv\\Scripts\\Activate.ps1"
