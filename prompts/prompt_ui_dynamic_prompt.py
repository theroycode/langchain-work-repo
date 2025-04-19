from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Ai tutor")

topic_input = st.text_input("Enter the topic you want a summary for (e.g., 'Convolution', 'Optical Fiber', etc.)")

subject_input = st.text_input("Enter the subject this topic belongs to (e.g., 'Digital Signal Processing', 'Optical Communication')")

depth_input = st.selectbox(
    "Select Explanation Depth",
    ["Quick Insight", "Focused Clarity", "Deep Dive"]
)

template = load_prompt("template.json")

if topic_input and subject_input:
    prompt = template.invoke({
        "topic_input": topic_input,
        "subject_input": subject_input,
        "depth_input": depth_input
    })

model_choice = st.selectbox(
    "Choose Model for answer",
    ["Gemini 2.5 Flash", "Gemini 2.5 Pro"]
)



if st.button("summarize"):
    placeholder = st.empty()
    full_response = ""

    if model_choice == "Gemini 2.5 Pro":
        model = ChatGoogleGenerativeAI(model="gemini-2.5-pro-exp-03-25")
    else:
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17")

    for chunk in model.stream(prompt):
        full_response += chunk.content
        placeholder.markdown(full_response, unsafe_allow_html=True)



