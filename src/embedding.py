import os
import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from exception import customexception
from logger import logging
from data_ingestion import load_data

def chunk_data():
    try:
        logging.info("Loading local embedding model...")
        
        # Local embedding model - no API needed
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )

        # Load and chunk documents
        documents = load_data('./data/')
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            length_function=len
        )
        docs = text_splitter.split_documents(documents)
        
        # Create vector store
        vector_store = FAISS.from_documents(docs, embeddings)
        logging.info(f"Created vector store with {len(docs)} chunks")
        
        return vector_store, docs

    except Exception as e:
        logging.error(f"Error in embedding generation: {e}")
        raise customexception(e, sys)