from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system','You are an helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('user','{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'where is my refund'})

print(prompt)
