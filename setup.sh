#!/bin/bash

echo "Setting up the PDF Chatbot..."

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies for backend
echo "Installing backend dependencies..."
pip install -r backend/requirements.txt

# Install dependencies for frontend
echo "Installing frontend dependencies..."
pip install -r frontend/requirements.txt

echo "Setup complete! Run the chatbot using:"
echo "  - Start API: source venv/bin/activate && python backend/app.py"
echo "  - Start UI: source venv/bin/activate && streamlit run frontend/app.py"
