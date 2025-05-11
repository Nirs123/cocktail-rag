import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd
import sqlite3

model = SentenceTransformer('all-MiniLM-L6-v2')

conn = sqlite3.connect('streamlit_app/database.db')
query = 'SELECT * FROM cocktails'
cocktails_df = pd.read_sql_query(query, conn)

cocktails_df['vector_decode'] = cocktails_df['vector'].apply(lambda x: np.frombuffer(x, dtype=np.float32))

def get_embedding(text):
    return model.encode(text)

def euclidian_distance(v1: np.ndarray, v2: np.ndarray):
    return np.linalg.norm(v1 - v2)

def get_closest_cocktails(input: str):
    input_vector = get_embedding(input)
    cocktails_df[input] = cocktails_df['vector_decode'].apply(lambda x: euclidian_distance(input_vector, x))
    relevant_cocktails = cocktails_df.sort_values(by=input).head(10)['name'].tolist()

    new_cocktail_df = cocktails_df[cocktails_df['name'].isin(relevant_cocktails)]
    
    return new_cocktail_df.to_dict(orient='records')
