import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"  # Change this if using a deployed API

st.title("Check bylaws")
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{API_URL}/upload", files=files)

    if response.status_code == 200:
        st.success("PDF uploaded and processed successfully!")
    else:
        st.success("fa")

query = st.text_input("Ask a question:")
if st.button("Submit"):
    if query:
        data = {"query": query}
        response = requests.post(f"{API_URL}/ask", json=data)
        if response.status_code == 200:
            st.write("Chatbot:", response.json()["response"])
        else:
            st.warning("Error fetching response.")
    else:
        st.warning("Please enter a question.")
