from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """
    This function initializes the embedding model.
    It uses a lightweight 'sentence-transformer' that runs locally 
    on your CPU, so it's free and fast.
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )