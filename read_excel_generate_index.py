import pandas as pd
import re
import pickle

import faiss
from generate_embeddings import generate_embedding

from vector_store import VectorStore

store = VectorStore()

def read_excel_generate_index():
    data = pd.read_excel('E:/Downloads/viosa/interview_data.xlsx')

    url_pattern = r'https?://\S+'
    # Create a dictionary to store cell references and their corresponding embeddings
    # embedding_dict = {}

    # Iterate through all rows and columns and print the cell index and content
    for row_index, row in data.iterrows():
        for col_index, cell_content in enumerate(row):
            # Check if the cell is not empty, does not contain a URL, and contains more than one word
            if (not pd.isnull(cell_content) and
                not re.search(url_pattern, str(cell_content)) and
                len(str(cell_content).split()) > 1):
                # print(f"Cell ({row_index}, {col_index}): {cell_content}")
                print(f"Generating and storing embedding for {cell_content}")                
                store.add_to_store(str(row_index) + "," + str(col_index), cell_content)
    
    print("Storing FAISS index...")
    faiss.write_index(store.create_index(), 'index.faiss')
    
    print("Creating pkl dump...")
    with open('dump.pkl', "wb") as file:
        pickle.dump(store, file)
        file.close()


if __name__ == "__main__":
    read_excel_generate_index()