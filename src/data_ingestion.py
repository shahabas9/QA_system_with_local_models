import os
import sys
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders.directory import DirectoryLoader
from logger import logging
from exception import customexception

def load_data(data_path):
    """
    Load PDF documents from specified directory
    """
    try:
        logging.info("Data loading started...")
        loader = DirectoryLoader(
            data_path, 
            glob="**/*.pdf", 
            loader_cls=PyPDFLoader,
            show_progress=True
        )
        documents = loader.load()
        logging.info(f"Loaded {len(documents)} documents from {data_path}")
        return documents
    except Exception as e:
        logging.error(f"Exception in loading data: {e}")
        raise customexception(e, sys)