from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-preview-04-17')

st.header("Research tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

prompt = template.invoke({
    "length_input":length_input,
    "paper_input":paper_input,
    "style_input":style_input
})

if st.button("summarize"):
    placeholder = st.empty()
    full_response = ""

    for chunk in model.stream(prompt):
        full_response += chunk.content
        placeholder.markdown(full_response, unsafe_allow_html=True)



