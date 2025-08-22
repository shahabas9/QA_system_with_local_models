import streamlit as st
from qa_chain import setup_qa_chain
from logger import logging

# Initialize QA system
@st.cache_resource(show_spinner=False)
def init_qa():
    try:
        logging.info("Initializing local RAG system...")
        qa = setup_qa_chain()
        logging.info("✅ System initialized successfully!")
        return qa
    except Exception as e:
        logging.error(f"❌ Initialization failed: {e}")
        return None

qa_chain = init_qa()

# ---- Streamlit UI ----
st.set_page_config(page_title="RAG QA System", page_icon="🤖", layout="centered")

st.title("🤖 RAG QA System")
st.write("Ask a question based on your documents")

if qa_chain is None:
    st.error("❌ System initialization failed. Please check the logs.")
else:
    # Chat interface
    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.chat_input("Type your question here...")

    if user_input:
        st.session_state.history.append({"role": "user", "content": user_input})

        try:
            logging.info(f"📩 User question: {user_input}")
            result = qa_chain({"query": user_input})
            response = result['result']

            if "i'm not sure" in response.lower():
                response = "I'm not sure, please contact human support."

            logging.info(f"📤 Bot response: {response}")
            st.session_state.history.append({"role": "assistant", "content": response})

        except Exception as e:
            logging.error(f"❌ Error in chat: {e}")
            st.session_state.history.append(
                {"role": "assistant", "content": "⚠️ I'm experiencing technical difficulties. Please try again."}
            )

    # Render chat messages
    for msg in st.session_state.history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
