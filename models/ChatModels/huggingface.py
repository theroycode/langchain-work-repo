from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Create a roadmap that gets AIR 1 in gate cse 2026 in 10months")

print(result.content)