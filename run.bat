@echo off
echo Starting RAG QA System...
echo.

REM Activate virtual environment
call rag_env\Scripts\activate.bat

REM Run the application
echo Starting server at http://localhost:5000
echo Press Ctrl+C to stop
echo.
python src\app.py

pause