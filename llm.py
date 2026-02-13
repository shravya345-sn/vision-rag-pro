from groq import Groq
from config import Config

def get_answer(query, context):
    """The 'Brain' that synthesizes text and visual context."""
    client = Groq(api_key=Config.GROQ_API_KEY)
    
    # SYSTEM PROMPT: Establishes role and reasoning logic
    system_message = (
        "You are a Senior Technical Analyst. You have been provided with 'Context' "
        "which includes text from PDFs and 'DETAILED VISUAL ANALYSIS' from images. "
        "RULE 1: Treat visual analysis as direct observation. Do not say 'I cannot see it.' "
        "RULE 2: If the user asks about a diagram, use the visual analysis to explain it. "
        "RULE 3: Cross-reference text and images to provide the most accurate answer. "
        "RULE 4: Cite the specific file names provided in the context."
    )

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"CONTEXT FOR ANALYSIS:\n{context}\n\nUSER QUESTION: {query}"}
        ],
        model=Config.LLM_MODEL,
        temperature=0.3
    )
    return response.choices[0].message.content