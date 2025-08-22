import os
from langchain.llms import HuggingFacePipeline
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from logger import logging

def load_local_llm():
    """
    Load local open-source LLM for QA tasks
    """
    try:
        logging.info("Loading local FLAN-T5 model...")
        
        # Using FLAN-T5 - excellent for instruction following and QA
        model_name = "google/flan-t5-base"
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        # Create text generation pipeline
        pipe = pipeline(
            "text2text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=256,
            do_sample=False,
            temperature=0.1,
            repetition_penalty=1.1
        )
        
        llm = HuggingFacePipeline(pipeline=pipe)
        logging.info(f"Successfully loaded local model: {model_name}")
        
        return llm
        
    except Exception as e:
        logging.error(f"Error loading local model: {e}")
        raise e