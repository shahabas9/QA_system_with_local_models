from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from model_loader import load_local_llm
from embedding import chunk_data
from logger import logging

def setup_qa_chain():
    try:
        logging.info("Setting up local QA chain...")
        
        # Load local LLM
        llm = load_local_llm()
        
        # Create vector store with embeddings
        vector_store, docs = chunk_data()
        
        # Create prompt template optimized for local models
        prompt_template = """
        Answer the question based only on the context provided below.
        
        If the answer cannot be found in the context, say exactly: 
        "I'm not sure, please contact human support."
        
        Do not use any external knowledge or make up information.
        
        Context: {context}
        
        Question: {question}
        
        Answer:
        """
        
        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 4}
            ),
            chain_type_kwargs={"prompt": PROMPT},
            return_source_documents=True
        )
        
        logging.info("Local QA chain setup completed successfully!")
        return qa_chain
        
    except Exception as e:
        logging.error(f"Error setting up QA chain: {e}")
        raise e