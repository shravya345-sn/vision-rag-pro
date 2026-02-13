import streamlit as st
from PyPDF2 import PdfReader
# UPDATED: Removed 'rag.' prefix because your files are in the main folder
from retriever import process_documents, search_context
from llm import get_answer
from vision import get_image_description
import os

# 1. PAGE CONFIG & MODERN UI
st.set_page_config(page_title="VisionRAG Pro", layout="wide", page_icon="🧠")

st.markdown("""
    <style>
    /* Main Background & Text Visibility Fix */
    .stApp { background: linear-gradient(135deg, #0f0c29 0%, #302b63 100%); color: #ffffff !important; }
    
    /* CHAT BUBBLE FIX: High contrast text and glassmorphism */
    .stChatMessage { background: rgba(255, 255, 255, 0.1) !important; border-radius: 15px !important; border: 1px solid rgba(0, 210, 255, 0.3) !important; margin-bottom: 10px !important; padding: 10px !important; }
    .stChatMessage p, .stChatMessage span, .stChatMessage div { color: #ffffff !important; font-size: 1rem !important; }

    /* WHITE BLANK FIX: Removing excessive top padding */
    .block-container { padding-top: 1.5rem !important; padding-bottom: 0rem !important; }
    
    /* SIDEBAR styling */
    section[data-testid="stSidebar"] { background-color: rgba(0, 0, 0, 0.4) !important; backdrop-filter: blur(10px); }
    
    /* CODE BLOCK visibility fix */
    code { background-color: #2e2e2e !important; color: #00ff00 !important; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 2. STATE MANAGEMENT
if "messages" not in st.session_state: st.session_state.messages = []
if "vector_db" not in st.session_state: st.session_state.vector_db = None

# 3. SIDEBAR: MULTI-FILE SOURCE TRACKING
with st.sidebar:
    st.title("📂 Knowledge Base")
    uploaded_pdfs = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
    uploaded_images = st.file_uploader("Upload Images", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    if st.button("🚀 Global Sync"):
        pdf_pairs = []
        img_pairs = []
        
        # Process PDFs
        for pdf in uploaded_pdfs:
            reader = PdfReader(pdf)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            pdf_pairs.append((pdf.name, text))
        
        # Process Images
        for img in uploaded_images:
            with st.spinner(f"AI 'Scanning' {img.name}..."):
                # Temporary file handling for cloud environment
                with open("temp_img.jpg", "wb") as f:
                    f.write(img.getbuffer())
                desc = get_image_description("temp_img.jpg")
                img_pairs.append((img.name, desc))
        
        if pdf_pairs or img_pairs:
            with st.spinner("Building Intelligent Brain..."):
                # preserves document identity
                st.session_state.vector_db = process_documents(pdf_pairs, img_pairs)
            st.success("Global Brain Synced with Source Tracking!")
            st.balloons()
        else:
            st.warning("Please upload files first.")

    if st.button("🗑️ Reset Assistant"):
        st.session_state.messages = []; st.session_state.vector_db = None; st.rerun()

# 4. MAIN CHAT
st.title("💬 Intelligence Hub")

# Display historical messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about your files..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if st.session_state.vector_db:
        with st.chat_message("assistant"):
            with st.spinner("Analyzing cross-document context..."):
                # Search across all uploaded sources
                context = search_context(prompt, st.session_state.vector_db)
                response = get_answer(prompt, context)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.info("Upload and 'Sync' files in the sidebar to begin.")

