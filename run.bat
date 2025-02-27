@echo off
echo Starting the PDF Chatbot...

:: Activate virtual environment
call venv\Scripts\activate

:: Start Flask API in the background
start cmd /k "python backend\app.py"

:: Wait for API to start
timeout /t 5

:: Start Streamlit UI
start cmd /k "streamlit run frontend\app.py"
