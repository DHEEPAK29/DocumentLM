@echo off
echo Setting up the PDF Chatbot...

:: Create virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install dependencies
echo Installing backend dependencies...
pip install -r backend/requirements.txt

echo Installing frontend dependencies...
pip install -r frontend/requirements.txt

echo Setup complete! Run the chatbot using:
echo  - Start API: venv\Scripts\activate & python backend\app.py
echo  - Start UI: venv\Scripts\activate & streamlit run frontend\app.py
pause
