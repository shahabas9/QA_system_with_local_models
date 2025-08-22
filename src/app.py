from flask import Flask, render_template, request, jsonify
from qa_chain import setup_qa_chain
from logger import logging
import os,sys
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # one level up from src
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR,"static")
app = Flask(__name__, template_folder=TEMPLATE_DIR,static_folder=STATIC_DIR)
# Initialize the QA system
try:
    logging.info("Initializing local RAG system...")
    qa_chain = setup_qa_chain()
    logging.info("✅ System initialized successfully!")
except Exception as e:
    logging.error(f"❌ Initialization failed: {e}")
    qa_chain = None

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def chat():
    if qa_chain is None:
        return "System initialization failed. Please check the logs."
    
    try:
        user_input = request.form['msg'].strip()
        
        if not user_input:
            return "Please enter a question."
        
        logging.info(f"📩 User question: {user_input}")
        
        # Get response from local QA chain
        result = qa_chain({"query": user_input})
        response = result['result']
        
        # Clean up response
        if "i'm not sure" in response.lower():
            response = "I'm not sure, please contact human support."
        
        logging.info(f"📤 Bot response: {response}")
        
        return response
        
    except Exception as e:
        logging.error(f"❌ Error in chat: {e}")
        return "I'm experiencing technical difficulties. Please try again."

if __name__ == '__main__':
    print("🌐 Starting RAG QA System...")
    print("📖 Open http://localhost:5000 in your browser")
    print("⏹️  Press Ctrl+C to stop")
    app.run(host='0.0.0.0', port=5000, debug=False)