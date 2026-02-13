import os
from dotenv import load_dotenv

# Load your API key from the .env file
load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # UPDATED: Using the supported Llama 4 Scout model for Vision
    VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct" 
    
    # Using Llama 3.3 for high-quality text generation
    LLM_MODEL = "llama-3.3-70b-versatile"         
    
    # This is the local model used to turn text into searchable numbers
    EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"