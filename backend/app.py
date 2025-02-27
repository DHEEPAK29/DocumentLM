import os
import faiss
import PyPDF2
import numpy as np
from sentence_transformers import SentenceTransformer
from flask import Flask, request, jsonify
from flask_cors import CORS  # Allow frontend to access API

app = Flask(__name__)
CORS(app)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + " "
    return text

def create_vector_store(text_chunks):
    embeddings = np.array([embedding_model.encode(chunk) for chunk in text_chunks], dtype=np.float32)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index, text_chunks

def retrieve_relevant_chunk(query, index, text_chunks):
    query_embedding = np.array([embedding_model.encode(query)], dtype=np.float32)
    _, indices = index.search(query_embedding, 1)
    return text_chunks[indices[0][0]]

# API route to upload PDF
@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    
    text = extract_text_from_pdf(file_path)
    text_chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    
    global index, stored_chunks
    index, stored_chunks = create_vector_store(text_chunks)
    
    return jsonify({"message": "PDF uploaded and processed successfully"})

# API route to handle user queries
@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    query = data.get("query")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    answer = retrieve_relevant_chunk(query, index, stored_chunks)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
