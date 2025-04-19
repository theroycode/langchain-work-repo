import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load your .env once
load_dotenv()  # GOOGLE_API_KEY must be in your .env

# Instantiate your model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17")

#  Streamlit page config
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("💬 Your personal Chat Buddy!!!")

#  Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

#  Render existing messages
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

#  Capture new user input
user_text = st.chat_input("You:")

if user_text:
    # add user turn to history & UI
    st.session_state.chat_history.append(HumanMessage(content=user_text))
    with st.chat_message("user"):
        st.markdown(user_text)

    # prepare assistant bubble for streaming
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        for chunk in model.stream(st.session_state.chat_history):
            full_response += chunk.content
            placeholder.markdown(full_response, unsafe_allow_html=True)

    # finally, save assistant turn
    st.session_state.chat_history.append(AIMessage(content=full_response))
