from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings= GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07")
result = embeddings.embed_query("Hello world")
print(result)
print(len(result))