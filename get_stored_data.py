import pickle
import faiss

faiss_index = faiss.read_index("index.faiss")

with open('dump.pkl', 'rb') as file:
    loaded_vector_store = pickle.load(file)
