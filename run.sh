#!/bin/bash
echo "Starting RAG QA System..."
echo

# Activate virtual environment
source rag_env/bin/activate

# Run the application
echo "Starting server at http://localhost:5000"
echo "Press Ctrl+C to stop"
echo
python src/app.py