from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-2",dimensions=300)
documents=[
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
]

query='tell me about Paris'
doc_embeddings=embedding.embed_documents(documents)
query_embeddings=embedding.embed_query(query)

scores = cosine_similarity([query_embeddings],doc_embeddings)[0]
index, score= (sorted(list(enumerate(scores)),key=lambda x:x[1])[-1])
print(query)
print(documents[index])
print("Similarity Score:",score)