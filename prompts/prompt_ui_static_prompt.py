from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-preview-04-17')

st.header("Research tool")


user_input = st.text_input("Write your query : [powered by gemini 2.5 flash (latest)]")

if st.button("Send"):
    result=model.invoke(user_input)
    st.write(result.content)



