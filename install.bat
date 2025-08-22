@echo off
echo Installing RAG QA System...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if not errorlevel 1 (
    echo Python is already installed.
    goto :install_deps
)

python3 --version >nul 2>&1
if not errorlevel 1 (
    echo Python3 is already installed.
    goto :install_deps
)

echo Python is not installed. Installing Python 3.10...
echo.

REM Download and install Python silently
echo Downloading Python installer...
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe' -OutFile 'python_installer.exe'"

echo Installing Python (this may take a few minutes)...
start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

REM Clean up installer
del python_installer.exe

REM Check if Python installation was successful
python --version >nul 2>&1
if errorlevel 1 (
    echo Failed to install Python automatically.
    echo Please install Python manually from https://python.org
    echo Then run this installer again.
    pause
    exit /b 1
)

:install_deps
echo Python installed successfully!
echo.

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