import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("./model/multi-qa-MiniLM-L6-cos-v1", device="cpu")

def generate_embedding(text):
    response = model.encode([text])  # Encode the text using the pre-trained model
    return np.array(response[0])  # Return the generated embedding as a NumPy array