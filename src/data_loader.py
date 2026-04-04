from pathlib import Path
from typing import List, Dict, Any
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.document_loaders import  Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader

def load_all_documents(data_dir: str) -> List[Dict[str, Any]]:
    """Load all documents from the specified directory and return a list of dicts with content and metadata."""
    
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data Path: {data_path}")
    documents = []

    # PDF files
    pdf_files = list(data_path.glob("**/*.pdf"))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files: {[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file}: {e}")

    return documents

    # Text files
    text_files = list(data_path.glob("**/*.txt"))   
    print(f"[DEBUG] Found {len(text_files)} Text files: {[str(f) for f in text_files]}")
    for text_file in text_files:
        print(f"[DEBUG] Loading Text: {text_file}")
        try:
            loader = TextLoader(str(text_file))
            loaded = loader.load()
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load Text {text_file}: {e}")