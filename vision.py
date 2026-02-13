import base64
from groq import Groq
from config import Config

def encode_image(image_path):
    """Encodes a local image to base64 for Groq API."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def get_image_description(image_path):
    """Force high-detail, technical analysis of the image."""
    client = Groq(api_key=Config.GROQ_API_KEY)
    base64_image = encode_image(image_path)

    # UPDATED INSTRUCTIONS: Lead with the "must-do" for deeper analysis
    detailed_prompt = (
        "Perform a deep technical analysis of this image. "
        "1. Identify all text, diagrams, flowcharts, and labels. "
        "2. If it's a chart or table, transcribe the data exactly. "
        "3. Describe the logical flow, relationships between objects, and technical intent. "
        "4. Note any colors or visual cues that imply hierarchy or state. "
        "Be precise and technical. Avoid vague summaries."
    )

    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": detailed_prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ],
        }],
        model=Config.VISION_MODEL,
        temperature=0.1  # Lower temperature for higher factual precision
    )
    
    # Labeling the output clearly for the RAG brain
    return f"[DETAILED VISUAL ANALYSIS]: {chat_completion.choices[0].message.content}"