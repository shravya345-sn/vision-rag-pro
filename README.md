# vision-rag-pro
A professional-grade Multimodal RAG application featuring cross-document intelligence, deep visual analysis via Groq Vision, and persistent conversational memory

🌟 Overview
VisionRAG Pro is an advanced Multimodal Retrieval-Augmented Generation (RAG) platform designed to bridge the gap between textual data and visual intelligence. While standard RAG systems are often "blind" to non-textual data, this project synchronizes high-fidelity PDF text extraction with deep semantic analysis of complex images, such as flowcharts, architectural diagrams, and technical tables.


Live Demo
The application is deployed and accessible here:
https://vision-rag-pro-nwhyckmthdm6bqh8adaxau.streamlit.app/


🛠️ The Problem it Solves
In many technical domains, critical information is trapped inside images (e.g., system designs or data charts) that standard LLMs cannot access through text-only RAG pipelines. VisionRAG Pro solves this by analyzing these visual assets and converting them into searchable, technical descriptions that are stored in a unified vector database.

🧠 How It Works (The Pipeline)
The system follows a three-stage intelligent workflow:

Multimodal Ingestion: PDFs are parsed into text chunks, while images are processed by a Vision-capable LLM (via Groq) to generate detailed, context-aware descriptions.

Hybrid Vector Storage: Both text and image data are embedded and stored in a FAISS vector store, allowing the system to perform high-speed semantic searches across different data types.

Context-Aware Synthesis: When a user asks a question, the system retrieves the most relevant text and image context. A reasoning LLM (Llama 3.3) then synthesizes this data to provide a grounded, expert-level response.

✨ Key Features
Unified Intelligence: Simultaneously search through PDF documents and image libraries.

Source-Aware Citations: The assistant identifies exactly which document or image it used to generate its answer.

Modern Interface: Built with a custom Streamlit UI featuring glassmorphism and high-contrast visuals for a professional user experience.

High-Speed Inference: Optimized for the Groq LPU Inference Engine, ensuring near-instant response times for complex multimodal queries.


FOLDER STRUCTURE 

vision-rag-pro/
├── app.py
├── retriever.py
├── llm.py
├── vision.py
├── embeddings.py
├── requirements.txt
├── README.md
└── .gitignore



