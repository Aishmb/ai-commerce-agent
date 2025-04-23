from sentence_transformers import SentenceTransformer
import numpy as np

# Load the pre-trained model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def encode_text(text: str):
    return model.encode(text)
