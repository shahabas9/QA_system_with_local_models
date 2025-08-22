#!/bin/bash
echo "Installing RAG QA System..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3.10"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv rag_env

# Activate and install dependencies
echo "Installing dependencies..."
source rag_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo
echo "Installation complete!"
echo "To run the system, execute: source run.sh"