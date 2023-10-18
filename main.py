import numpy as np
import pickle
import faiss 

from generate_embeddings import generate_embedding
from read_source_file import read_source_file
from get_stored_data import faiss_index, loaded_vector_store

query_embedding = generate_embedding("Can you share an example from your academics or internship experience, where you had to work as part of a team to complete a complex project? What was your role and how did you handle disagreements or conflicts within the team?")

# query_embedding = generate_embedding("Tell me about a time when you had to work with a team member who was not contributing effectively. How did you handle the situation?")
# print(query_embedding)

# source_file = "E:/Development/node/speech-recognition/output.txt"
# source_dict = read_source_file(source_file)
# print(source_dict)

distances, indexes = faiss_index.search(np.array([query_embedding], dtype=np.float32), 2)

matching_sentences = [loaded_vector_store.sentences[i] for i in indexes[0]]
matching_cell = [loaded_vector_store.cell_references[i] for i in indexes[0]]
print(matching_sentences)
print(matching_cell)
# add offset of 2 to the column val

# Can you share an example from your academics or internship experience, where you had to work as part of a team to complete a complex project? What was your role and how did you handle disagreements or conflicts within the team?
# Can you share an example from your academic or internship experience where you had to work as part of a team to complete a complex project? What was your role, and how did you handle disagreements or conflicts within the team?
