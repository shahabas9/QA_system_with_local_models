@echo off
echo Installing RAG QA System...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.10 from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv rag_env

REM Activate and install dependencies
echo Installing dependencies...
call rag_env\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Installation complete!
echo To run the system, double-click 'run.bat'
pause