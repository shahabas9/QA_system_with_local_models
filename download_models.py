#!/usr/bin/env python3
"""
Pre-download models to avoid first-run delays
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModel
from sentence_transformers import SentenceTransformer
import logging

logging.basicConfig(level=logging.INFO)

def download_models():
    """Download all required models upfront"""
    models_to_download = [
        # LLM for QA
        ("google/flan-t5-base", AutoTokenizer, AutoModelForSeq2SeqLM),
        # Embedding model
        ("sentence-transformers/all-MiniLM-L6-v2", None, None),
    ]
    
    for model_name, tokenizer_class, model_class in models_to_download:
        try:
            logging.info(f"Downloading {model_name}...")
            
            if tokenizer_class and model_class:
                # Download tokenizer and model
                tokenizer = tokenizer_class.from_pretrained(model_name)
                model = model_class.from_pretrained(model_name)
                logging.info(f"✓ Downloaded {model_name}")
            else:
                # Download sentence transformer
                model = SentenceTransformer(model_name)
                logging.info(f"✓ Downloaded {model_name}")
                
        except Exception as e:
            logging.error(f"Failed to download {model_name}: {e}")

if __name__ == "__main__":
    download_models()
    print("Model download completed!")