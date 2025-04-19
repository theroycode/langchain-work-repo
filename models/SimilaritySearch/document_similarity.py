from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07")

document = [
    "Micheal phelps is a great swimmer",
    "Micheal phelps has highest number of medals in olympics",
    "Micheal jordan is the finest basketball player",
    "Del steyn was the best pacer of his time",
    "But mitchell starc is best pacer according to me"
]
query = input("what is your query?: ")

doc_vectors = embedding.embed_documents(document)
query_vectors = embedding.embed_query(query)

similarity_scores = cosine_similarity([query_vectors] , doc_vectors)

print(document[np.argmax(similarity_scores, axis=1)[0]])





