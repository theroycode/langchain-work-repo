from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-preview-04-17')

message= input("Ask your query")

for chunk in model.stream(message):
    print(chunk.content)