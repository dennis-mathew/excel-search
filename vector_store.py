import faiss
import numpy as np

from generate_embeddings import generate_embedding


class VectorStore:
  
  def __init__(self):
    self.cell_references = []
    self.sentences = []
    self.embeddings = None
    # np.empty((0,384))  # Initialize as empty array
    # multi-qa-MiniLM-L6-cos-v1 Sentence Transformers model provides a vector with 384 dimensions.

  def add_to_store(self,cell_reference,  sentence):
    # Append the document to the list of documents
    self.cell_references.append(cell_reference)
    self.sentences.append(sentence)
    # Generate the embedding for the document
    embedding = generate_embedding(sentence)
    if self.embeddings is None:
      self.embeddings = np.array([embedding])
    else: 
      # Concatenate the response with the existing embeddings vertically
      self.embeddings = np.vstack((self.embeddings, embedding))

  def create_index(self):
    index = faiss.IndexFlatL2(self.embeddings.shape[1])
    index.add(self.embeddings)
    return index
