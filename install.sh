#!/bin/bash
echo "Installing RAG QA System..."
echo

# Check if Python is installed
if command -v python3 &> /dev/null; then
    echo "Python3 is already installed."
    python3 --version
elif command -v python &> /dev/null; then
    echo "Python is already installed."
    python --version
else
    echo "Python is not installed."
    echo
    echo "Please install Python 3.8 or higher using your package manager:"
    echo
    echo "For Ubuntu/Debian:"
    echo "  sudo apt update && sudo apt install python3 python3-pip python3-venv"
    echo
    echo "For CentOS/RHEL:"
    echo "  sudo yum install python3 python3-pip"
    echo
    echo "For Mac:"
    echo "  brew install python"
    echo
    echo "After installing Python, run this script again."
    exit 1
fi

# Determine which Python command to use
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Python not found even after check. Please install Python."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $PYTHON_VERSION"

# Verify Python version is 3.8 or higher
if [[ $(echo "$PYTHON_VERSION < 3.8" | bc -l) -eq 1 ]]; then
    echo "Error: Python 3.8 or higher is required. Found version $PYTHON_VERSION"
    echo "Please upgrade your Python installation."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
$PYTHON_CMD -m venv rag_env

# Activate and install dependencies
echo "Installing dependencies..."
source rag_env/bin/activate

# Upgrade pip first
pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Error: requirements.txt not found!"
    deactivate
    exit 1
fi

echo
echo "✅ Installation complete!"
echo
echo "To run the system:"
echo "  source run.sh"
echo
echo "Or manually:"
echo "  source rag_env/bin/activate"
echo "  python src/app.py"
echo
