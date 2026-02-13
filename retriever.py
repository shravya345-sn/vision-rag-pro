from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from rag.embeddings import get_embedding_model

def process_documents(pdf_data_list, image_data_list):
    """
    pdf_data_list: List of tuples (filename, text)
    image_data_list: List of tuples (filename, description)
    """
    all_docs = []

    # Tag PDF text with source filename
    for filename, text in pdf_data_list:
        all_docs.append(Document(page_content=text, metadata={"source": filename}))

    # Tag Image descriptions with source filename
    for filename, desc in image_data_list:
        all_docs.append(Document(page_content=desc, metadata={"source": filename}))

    # Split documents while preserving the metadata tags
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    final_docs = text_splitter.split_documents(all_docs)

    embeddings = get_embedding_model()
    return FAISS.from_documents(final_docs, embeddings)

def search_context(query, vector_db):
    """Retrieves context and labels each part with its source for the AI."""
    docs = vector_db.similarity_search(query, k=4)
    
    context_with_labels = ""
    for doc in docs:
        source = doc.metadata.get("source", "Unknown Source")
        context_with_labels += f"\n---\nFROM FILE: {source}\nCONTENT: {doc.page_content}\n"
    
    return context_with_labels