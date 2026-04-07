# 📚 Traditional RAG Pipeline

A simple and modular **Retrieval-Augmented Generation (RAG)** pipeline that processes documents (PDFs/text), converts them into embeddings, stores them in a vector database, and enables retrieval-based question answering.

---

## 🚀 Features

- 📄 PDF & text document ingestion
- 🧹 Text preprocessing & chunking
- 🔍 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- 📦 Modular and extensible architecture

---

## 📁 Project Structure
.
├── data/
│ ├── pdf_files/ # Raw PDF documents
│ ├── text_files/ # Extracted or raw text files
│ ├── vector_store/ # Stored embeddings / vector DB
│
├── notebook/
│ ├── RAG_Pipeline.ipynb # End-to-end RAG workflow
│ ├── document.ipynb # Document processing experiments
│
├── src/ # Core source code (pipeline logic)
│
├── app.py # Main application entry point
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .gitignore


---

## ⚙️ How It Works


---

## ⚙️ How It Works

1. **Document Ingestion**
   - Load PDFs or text files from `data/pdf_files` or `data/text_files`

2. **Preprocessing**
   - Extract text
   - Clean and split into chunks

3. **Embedding Generation**
   - Convert chunks into vector embeddings

4. **Vector Storage**
   - Store embeddings in `data/vector_store`

5. **Retrieval**
   - Query relevant chunks using similarity search

6. **Generation**
   - Pass retrieved context to LLM for answer generation

7. **Tech Stack**
    - Python
    - Vector Database (FAISS )
    - LLM (OpenAI or similar)
    - Jupyter Notebooks
