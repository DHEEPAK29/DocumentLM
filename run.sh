#!/bin/bash

echo "Starting the PDF Chatbot..."

# Activate virtual environment
source venv/bin/activate

# Start the backend API in the background
echo "Starting Flask API..."
python backend/app.py &

# Wait for the API to start
sleep 5

# Start the frontend UI
echo "Starting Streamlit UI..."
streamlit run frontend/app.py
